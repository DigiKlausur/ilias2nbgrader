import os
from .preprocessor import Preprocessor
from traitlets import Unicode
from shutil import move
import glob

class CreateFolderStructure(Preprocessor):

    directory = Unicode('restructured', help='Subfolder where processed files go')
    
    def __init__(self):
        super(CreateFolderStructure, self).__init__()
    
    def mkdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
    
    def preprocess_student(self, student, resources):
        self.init_logging('Create Folder Structure')
        
        src = os.path.join(self.src, student)
        dst = os.path.join(self.dst, student, resources['assignment'])
        
        self.mkdir(os.path.join(self.dst, student))        
        move(src, dst)
        self.log.info('Moved submission to subfolder {}'.format(resources['assignment']))
        
        self.terminate_logging(os.path.join(self.dst, student, resources['assignment'], self.logname)) 
        
        return student, resources