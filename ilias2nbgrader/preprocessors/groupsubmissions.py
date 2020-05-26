from .preprocessor import Preprocessor
from ..utils import movefiles
from traitlets import Unicode
from nbformat.reader import NotJSONError
import os
import re
import nbformat
import glob

class GroupSubmissions(Preprocessor):
    
    directory = Unicode('grouped', help='Subfolder where renamed files go')
    
    def __init__(self):
        super(GroupSubmissions, self).__init__()
        self.__as_version = 4
        self.__p_student = re.compile('[a-z]+1?2s')
        
    def get_groups(self, students, resources):
        groups = dict()
        for student in students:
            nb_file = os.path.join(
                self.src,
                student, 
                resources['assignment'],
                resources['source_notebooks'][0]
            )
            try:
                nb = nbformat.read(nb_file, self.__as_version)
                group_cell = nb.cells[resources['group_cell']].source
                groups[student] = self.__p_student.findall(group_cell)
                if len(groups[student]) < 1:
                    groups[student] = [student]
            except NotJSONError:
                self.log.warning('Notebook {} is not JSON'.format(nb_file))
                groups[student] = [student]
            except FileNotFoundError:
                self.log.warning('No notebook for {}'.format(student))
                groups[student] = [student]
        return set([tuple(sorted(v)) for v in groups.values()])
    
    def get_notebook_size(self, student):
        size = 0
        for root, _, files in os.walk(os.path.join(self.src, student)):
            for file in files:
                if file.endswith('.ipynb'):
                    size += os.stat(os.path.join(root, file)).st_size
        return size
    
    def get_submissions(self, group, resources):
        submissions = []
        for member in group:
            path = os.path.join(self.src, member, resources['assignment'])
            if os.path.exists(path):
                submissions.append((self.get_notebook_size(member), member))
        return max(submissions)[1]
        
        
    def preprocess(self, path, resources):
        self.src = path
        self.dst = os.path.join(resources['path'], self.directory)
        students = [os.path.split(g)[-1] for g in glob.glob(os.path.join(self.src, '*'))]
        if 'group_cell' not in resources:
            return path, resources
        groups = self.get_groups(students, resources)
        for group in groups:
            self.init_logging('Group Submissions')
            group_name = '_'.join(group)
            leader = self.get_submissions(group, resources)
            src = os.path.join(self.src, leader)
            dst = os.path.join(self.dst, group_name)
            movefiles(src, dst)
            if len(group) > 1:
                self.log.info('Grouped students {}'.format(group))
            self.terminate_logging(os.path.join(self.dst, group_name, resources['assignment'], self.logname))

        if 'tmp_folders' not in resources:
            resources['tmp_folders'] = set([self.dst])
        else:
            resources['tmp_folders'].add(self.dst)
            
        return self.dst, resources
        