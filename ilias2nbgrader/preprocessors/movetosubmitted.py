import os
from .preprocessor import Preprocessor
from traitlets import Unicode
from ..utils import movefiles

class MoveToSubmitted(Preprocessor):

    directory = Unicode('submitted', help='Subfolder where processed files go')
    
    def __init__(self):
        super(MoveToSubmitted, self).__init__()
            
    def preprocess(self, path, resources):
        self.src = path
        self.dst = os.path.join(resources['course_dir'], self.directory)
        
        os.makedirs(self.dst, exist_ok=True)       

        movefiles(self.src, self.dst)
        return self.dst, resources