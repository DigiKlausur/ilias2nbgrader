import unittest
import os

class TestsBase(unittest.TestCase):


    def setUp(self):
        self.base_path = os.path.normpath('ilias2nbgrader/tests/preprocessors')
        self.file_path = os.path.join(self.base_path, 'files')
        self.course_dir = os.path.join(self.file_path, 'test_course')
        self.assignment = 'assignment_one'
        self.tmp_path = 'tmp'
        self.students = ['student1', 'student2', 'student3', 'student4']
        
        self.resources = {
            'course_dir': self.course_dir,
            'assignment': self.assignment,
            'path': self.tmp_path,
            'submission_zip': os.path.join(self.file_path, 'submissions.zip'),
            'feedback_zip': os.path.join(self.file_path, 'multi_feedback.zip')
        }