import os
from .preprocessor import Preprocessor
from traitlets import Unicode
from shutil import copytree, copy

class MoveToSubmitted(Preprocessor):

    directory = Unicode('submitted', help='Subfolder where processed files go')
    
    def __init__(self):
        super(MoveToSubmitted, self).__init__()

    def copyfiles(self, src, dst):
        for root, dirs, files in os.walk(src):
            dst_root = os.path.relpath(root, start=src)
            for file in files:
                os.makedirs(os.path.join(dst, dst_root), exist_ok=True)
                copy(os.path.join(root, file), os.path.join(dst, dst_root, file))
            for d in dirs:
                os.makedirs(os.path.join(dst, root, d), exist_ok=True)
            
    def preprocess(self, path, resources):
        self.src = path
        self.dst = os.path.join(resources['course_dir'], self.directory)
        
        os.makedirs(self.dst, exist_ok=True)       

        self.copyfiles(self.src, self.dst)
        return self.dst, resources