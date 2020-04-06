from rapidfuzz import fuzz
from .preprocessor import Preprocessor
import os

class RenameNotebooks(Preprocessor):
    
    def __init__(self):
        super(RenameNotebooks, self).__init__()
    
    def get_files(self, path, exclude=['.ipynb_checkpoints']):
        files = [(dp, f) for dp, dn, filenames in os.walk(path) \
                 for f in filenames]
        for ex in exclude:
            files = [f for f in files if ex not in os.path.join(f[0], f[1])]
        return [(f[0], f[1], f[1].split('.')[-1]) for f in files]
    
    def split(self, files):
        nbs = [f for f in files if f[-1] == 'ipynb']
        rest = [f for f in files if f[-1] != 'ipynb']
        return nbs, rest
    
    def get_matches(self, file, files):
        matches = [f for f in files if f[-1] == 'ipynb']
        sims = [fuzz.ratio(file[0], m[1]) for m in matches]
        best = sorted(range(len(sims)), key=sims[::-1].__getitem__)
        matches = list(map(lambda i: matches[i], best))
        sims = list(map(lambda i: sims[i], best))
        return matches, sims 
    
    def preprocess_student(self, student, resources):
        self.init_logging('Rename Notebooks')
        src_nbs = resources['source_notebooks']
        
        submission = os.path.join(self.src, student, resources['assignment'])
        submitted_notebooks, _ = self.split(self.get_files(submission))
        
        for src_nb in src_nbs:
            matches, _ = self.get_matches(src_nbs, submitted_notebooks)
            if len(matches) > 0:
                match = matches[0]
                if match[1] != src_nb:
                    src = os.path.join(match[0], match[1])
                    dst = os.path.join(match[0], src_nb)
                    os.rename(src, dst)
                    self.log.info('{}: Rename {} to {}'.format(student, match[1], src_nb)) 
                    
        self.terminate_logging(os.path.join(self.dst, student, resources['assignment'], self.logname)) 
        
        return student, resources
        
        
