import os
from shutil import copyfile
from .preprocessor import Preprocessor

class AddExtraFiles(Preprocessor):    
    
    def __init__(self):
        super(AddExtraFiles, self).__init__()
    
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