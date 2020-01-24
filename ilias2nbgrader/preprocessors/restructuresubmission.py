import glob
import os
import re
import nbformat
from traitlets import Unicode
from nbformat.reader import NotJSONError
from shutil import copyfile
from .preprocessor import Preprocessor


class RestructureSubmission(Preprocessor):

    directory = Unicode('adapted', help='Subfolder where processed files go') 
    
    def __init__(self):
        super(RestructureSubmission, self).__init__()
        self.__as_version = 4

    def __get_files(self, path, exclude=['.ipynb_checkpoints']):
        files = [os.path.join(base_path, file) for base_path, _, files in os.walk(path) \
                 for file in files]
        files = [os.path.relpath(file, start=path) for file in files]
        for ex in exclude:
            files = [file for file in files if ex not in file]
        nbs = [file for file in files if file.endswith('.ipynb')]
        other = [file for file in files if not file.endswith('.ipynb')]

        return nbs, other

    def __get_source(self, nb_file):
        try:
            nb = nbformat.read(nb_file, as_version=self.__as_version)
            return '\n'.join([cell.source for cell in nb.cells if cell.cell_type == 'code'])
        except NotJSONError:
            print('Notebook {} is not JSON'.format(nb_file))

    def __get_pattern(self, filename):
        r_dirname = r'[\w-]+'
        r_slash = r'(/|\\)'
        return re.compile(r'(({}{})*{})'.format(r_dirname, r_slash, filename))

    def __find_file(self, source, filename):
        return self.__get_pattern(filename).findall(source)

    def __find_files_in_notebook(self, nb_file, files):
        source = self.__get_source(nb_file)
        if source is None:
            return dict()
        finds = dict()
        for file in files:
            matches = self.__find_file(source, os.path.basename(file))
            entry = {
                'present': len(matches) > 0,
                'matches': matches
            }
            if len(matches) > 0:
                entry['relative'] = [os.path.join(m[1][:-1], os.path.basename(file)) for m in matches][0]
            else:
                entry['relative'] = file
            finds[file] = entry
        return finds

    def __mkdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def preprocess(self, path, resources):
        self.src = path
        self.dst = os.path.join(resources['path'], self.directory)
        students = [os.path.split(g)[-1] for g in glob.glob(os.path.join(self.src, '*'))]
        for student in students:
            self.preprocess_student(student, resources)
        if 'tmp_folders' not in resources:
            resources['tmp_folders'] = set([self.dst])
        else:
            resources['tmp_folders'].add(self.dst)
        return self.dst, resources

    def copyfinds(self, nb, src_base, dst_base, other, unused={}):
        nb_path = os.path.join(src_base, nb)
        finds = self.__find_files_in_notebook(nb_path, other)
        # Copy notebook
        copyfile(nb_path, os.path.join(dst_base, nb))

        for find in finds:
            src_file = os.path.join(src_base, find)
            if finds[find]['present']:
                if find in unused:
                    del unused[find]
                # Copy used file                    
                dst_file = os.path.join(dst_base, finds[find]['relative'])
                self.__mkdir(os.path.split(dst_file)[0])        
                copyfile(src_file, dst_file)
                
                if os.path.normpath(find) != os.path.normpath(finds[find]['relative']):
                    self.log.info('Moved {} to {}'.format(find, finds[find]['relative']))
            else:
                unused[find] = finds[find]
        return unused
    
    def preprocess_student(self, student, resources):
        self.init_logging('Restructure Submission')
       
        src_base = os.path.join(self.src, student, resources['assignment'])
        dst_base = os.path.join(self.dst, student, resources['assignment'])

        self.__mkdir(dst_base)
        unused = {}

        nbs, other = self.__get_files(src_base)

        for nb in nbs:
            unused = self.copyfinds(nb, src_base, dst_base, other, unused)

        # Copy unused files                    
        for file in unused:
            src_file = os.path.join(src_base, file)
            dst_file = os.path.join(dst_base, unused[file]['relative'])
            self.__mkdir(os.path.split(dst_file)[0])
            copyfile(src_file, dst_file)

        # Copy everything if no notebook was found
        if len(nbs) < 1:
            for file in other:
                src_file = os.path.join(src_base, file)
                dst_file = os.path.join(dst_base, file)
                self.__mkdir(os.path.split(dst_file)[0])
                copyfile(src_file, dst_file)
            
        self.terminate_logging(os.path.join(self.dst, student, resources['assignment'], self.logname))           
        return student, resources
