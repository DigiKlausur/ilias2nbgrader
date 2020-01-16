import glob
import os
import zipfile
from .preprocessor import Preprocessor


class ZipFeedback(Preprocessor):    
    
    def __init__(self):
        super(ZipFeedback, self).__init__()
    
    def preprocess(self, path, resources):
        self.src = path
        self.dst = os.path.join(resources['path'], resources['feedback_zip'])

        with zipfile.ZipFile(self.dst, 'w') as zf:
            for root, _, files in os.walk(self.src):
                for file in files:
                    src = os.path.join(root, file)
                    arcname = os.path.relpath(src, start=self.src)
                    zf.write(src, arcname)


        
        return resources['path'], resources