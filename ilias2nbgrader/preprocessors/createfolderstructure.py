import os
from .preprocessor import Preprocessor
from traitlets import Unicode
from shutil import copytree
import glob

class CreateFolderStructure(Preprocessor):

    directory = Unicode('restructured', help='Subfolder where processed files go')
    
    def __init__(self):
        super(CreateFolderStructure, self).__init__()
    
    def mkdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            
    def preprocess(self, path, resources):
        self.src = path
        self.dst = os.path.join(os.path.split(path)[0], self.directory)
        students = [os.path.split(g)[-1] for g in glob.glob(os.path.join(self.src, '*'))]
        for student in students:
            self.preprocess_student(student, resources)
        if 'tmp_folders' not in resources:
            resources['tmp_folders'] = set([self.dst])
        else:
            resources['tmp_folders'].add(self.dst)
        return self.dst, resources
    
    def preprocess_student(self, student, resources):
        self.init_logging('Create Folder Structure')
        
        src = os.path.join(self.src, student)
        dst = os.path.join(self.dst, student, resources['assignment'])
        
        self.mkdir(os.path.join(self.dst, student))        
        copytree(src, dst)
        self.log.info('Moved submission to subfolder {}'.format(resources['assignment']))
        
        self.terminate_logging(os.path.join(self.dst, student, resources['assignment'], self.logname)) 
        
        return student, resources