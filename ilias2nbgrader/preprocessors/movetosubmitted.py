import os
import glob
from .preprocessor import Preprocessor
from traitlets import Unicode
from shutil import copytree

class MoveToSubmitted(Preprocessor):

    directory = Unicode('submitted', help='Subfolder where processed files go')
    
    def __init__(self):
        super(MoveToSubmitted, self).__init__()
            
    def preprocess(self, path, resources):
        self.src = path
        self.dst = os.path.join(resources['course_dir'], self.directory)
        copytree(self.src, self.dst)
        return self.dst, resources