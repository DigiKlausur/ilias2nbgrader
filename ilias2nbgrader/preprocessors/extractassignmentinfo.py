import os
import glob
from .preprocessor import Preprocessor
from traitlets import Unicode
from shutil import copytree

class ExtractAssignmentInfo(Preprocessor):

    directory = Unicode('', help='Subfolder where processed files go')
    
    def __init__(self):
        super(ExtractAssignmentInfo, self).__init__()

    def get_files(self, path):
        nbs = []
        other = []
        for root, _, files in os.walk(path):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), start=path)
                if rel_path.endswith('.ipynb'):
                    nbs.append(rel_path)
                else:
                    other.append(rel_path)
        return nbs, other

            
    def preprocess(self, path, resources):
        source_path = os.path.join(resources['course_dir'], 'source', resources['assignment'])
        nbs, other = self.get_files(source_path)
        resources['source_notebooks'] = nbs
        resources['extra_files'] = {
            'base_path': source_path,
            'files': other
        }
        return path, resources