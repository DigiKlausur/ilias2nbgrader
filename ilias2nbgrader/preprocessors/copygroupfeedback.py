from .preprocessor import Preprocessor
from shutil import copyfile
import os
import re
import glob

class CopyGroupFeedback(Preprocessor):    
    
    def __init__(self):
        super(CopyGroupFeedback, self).__init__()
        self.__p_student = re.compile('[a-z]+1?2s')
        
    def get_groups(self, assignment):
        student_groups = dict()
        groups = [os.path.split(os.path.split(g)[0])[1] \
                  for g in glob.glob(os.path.join(self.src, '*', assignment))]
        
        for group in groups:
            for member in group.split('_'):
                student_groups[member] = group
                
        return student_groups
    
    def preprocess(self, path, resources):
        self.src = os.path.join(resources['course_dir'], 'feedback')
        self.dst = path
        student_groups = self.get_groups(resources['assignment'])
        students = [os.path.split(g)[-1] for g in glob.glob(os.path.join(self.dst, '*'))]
        
        for student in students:
            self.preprocess_student(student, student_groups, resources)
        if 'tmp_folders' not in resources:
            resources['tmp_folders'] = set([self.dst])
        else:
            resources['tmp_folders'].add(self.dst)
        
        return self.dst, resources
    
    def preprocess_student(self, student, groups, resources):
        matches = self.__p_student.findall(student)
        if len(matches) < 1 or matches[0] not in groups:
            return student, resources
        uid = matches[0]
        
        src_base = os.path.join(self.src, groups[uid], resources['assignment'])           
        dst_base = os.path.join(self.dst, student)   
        
        for nb in resources['source_notebooks']:
            filename = os.path.splitext(nb)[0] + '.html'
            feedback = os.path.join(src_base, filename)
            if os.path.isfile(feedback):
                copyfile(feedback, os.path.join(dst_base, filename))
        
        return student, resources