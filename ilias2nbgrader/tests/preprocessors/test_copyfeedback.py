import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import ExtractAssignmentInfo, ExtractFeedback, CopyFeedback

class TestCopyFeedback(TestsBase):

    def setUp(self):
        super().setUp()
        self.resources['course_dir'] = os.path.join(self.file_path, 'feedback_course')

    def test_copy_feedback(self):
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractFeedback().preprocess(path, resources)
        path, resources = CopyFeedback().preprocess(path, resources)
        assert os.path.exists(self.tmp_path)
        for student in self.students:
            assert os.path.exists(os.path.join(path, student))
            assert os.path.isfile(os.path.join(path, student, 'problem_set_one.html'))
        assert os.path.exists(os.path.join(path, 'student5'))
        assert not os.path.isfile(os.path.join(path, 'student5', 'problem_set_one.html'))

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            rmtree(self.tmp_path) 

if __name__ == '__main__':
    unittest.main()