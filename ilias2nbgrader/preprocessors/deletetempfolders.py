from .preprocessor import Preprocessor
from shutil import rmtree
import os

class DeleteTempFolders(Preprocessor):
       
    def preprocess(self, path, resources):
        if 'tmp_folders' in resources:
            removed = set()
            for folder in resources['tmp_folders']:
                if os.path.normpath(folder) != os.path.normpath(path):
                    rmtree(folder)
                    removed.add(folder)
                    self.log.info('Deleted folder {}'.format(folder))
            resources['tmp_folders'] -= removed
        if len(os.listdir(resources['path'])) < 1:
            rmtree(resources['path'])
        return path, resources