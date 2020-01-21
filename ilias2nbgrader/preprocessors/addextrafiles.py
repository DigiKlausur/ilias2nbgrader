import os
from shutil import copyfile
from .preprocessor import Preprocessor
import glob

class AddExtraFiles(Preprocessor):    
    
    def __init__(self):
        super(AddExtraFiles, self).__init__()
    
    def preprocess(self, path, resources):
        self.src = path
        self.dst = path
        students = [os.path.split(g)[-1] for g in glob.glob(os.path.join(self.src, '*'))]
        for student in students:
            self.preprocess_student(student, resources)
        if 'tmp_folders' not in resources:
            resources['tmp_folders'] = set([self.dst])
        else:
            resources['tmp_folders'].add(self.dst)
        return self.dst, resources
    
    def preprocess_student(self, student, resources):
        self.init_logging('Add Extra Files')
        
        if 'extra_files' not in resources:
            return student, resources
        
        dst_base = os.path.join(self.dst, student, resources['assignment'])
        
        extra_files = resources['extra_files']
        for file in extra_files['files']:
            src_file = os.path.join(extra_files['base_path'], file)
            dst = os.path.join(dst_base, file)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            
            copyfile(src_file, dst)
            self.log.info('Copied {} to {}'.format(os.path.split(file)[-1], file))
            
        self.terminate_logging(os.path.join(self.dst, student, resources['assignment'], self.logname))           
        return student, resources