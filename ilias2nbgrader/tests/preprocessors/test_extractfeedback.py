import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import ExtractFeedback

class TestExtractFeedback(TestsBase):

    def setUp(self):
        super().setUp()
        self.resources['course_dir'] = os.path.join(self.file_path, 'feedback_course')

    def test_extract_feedback(self):
        path, resources = ExtractFeedback().preprocess(self.tmp_path, self.resources)
        assert os.path.exists(self.tmp_path)

        for student in self.students:
            assert os.path.exists(os.path.join(path, student))
        assert os.path.exists(os.path.join(path, 'student5'))      

if __name__ == '__main__':
    unittest.main()