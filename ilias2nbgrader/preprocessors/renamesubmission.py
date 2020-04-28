from .preprocessor import Preprocessor
from ..utils import copyfiles
from traitlets import Unicode
import os
import re
import glob

class RenameSubmission(Preprocessor):
    
    directory = Unicode('renamed', help='Subfolder where renamed files go')
    
    def __init__(self):
        super(RenameSubmission, self).__init__()
        self.__p_student = re.compile('(?<=_)[a-z]+1?2s')
    
    def preprocess_student(self, student, resources):
        self.init_logging('Rename Submission')
        uid = self.__p_student.findall(student)[0]
        src = os.path.join(self.src, student)
        dst = os.path.join(self.dst, uid)
        if src != dst:
            self.log.info('Rename {} to {}'.format(student, uid))
        copyfiles(src, dst)
        self.terminate_logging(os.path.join(self.dst, uid, resources['assignment'], self.logname))