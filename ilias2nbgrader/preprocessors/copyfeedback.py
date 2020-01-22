import os
import glob
from shutil import copyfile
from .preprocessor import Preprocessor


class CopyFeedback(Preprocessor):    
    
    def __init__(self):
        super(CopyFeedback, self).__init__()
    
    def preprocess(self, path, resources):
        self.src = os.path.join(resources['course_dir'], 'feedback')
        self.dst = path
        students = [os.path.split(g)[-1] for g in glob.glob(os.path.join(self.dst, '*'))]
        for student in students:
            self.preprocess_student(student, resources)
        if 'tmp_folders' not in resources:
            resources['tmp_folders'] = set([self.dst])
        else:
            resources['tmp_folders'].add(self.dst)
        return self.dst, resources
    
    def preprocess_student(self, student, resources):        
        src_base = os.path.join(self.src, student, resources['assignment'])
        dst_base = os.path.join(self.dst, student)

        for nb in resources['source_notebooks']:
            filename = os.path.splitext(nb)[0] + '.html'
            feedback = os.path.join(src_base, filename)
            if os.path.isfile(feedback):
                copyfile(feedback, os.path.join(dst_base, filename))
        
        return student, resources
