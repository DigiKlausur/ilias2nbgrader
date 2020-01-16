from .preprocessor import Preprocessor
from traitlets import Unicode
import zipfile
import os

class Extract(Preprocessor):
    
    extract_path = Unicode('extracted', help='Subfolder to extract to')
    
    def __init__(self):
        super(Extract, self).__init__()
    
    def preprocess(self, path, resources):
        dst = os.path.join(path, self.extract_path)
        file = resources['submission_zip']
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(dst)
        if 'tmp_folders' not in resources:
            resources['tmp_folders'] = set([dst])
        else:
            resources['tmp_folders'].add(dst)
        return dst, resources