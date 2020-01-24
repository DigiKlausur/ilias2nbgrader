import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import ExtractAssignmentInfo, ExtractFeedback, CopyFeedback, ZipFeedback

class TestZipFeedback(TestsBase):

    def setUp(self):
        super().setUp()
        self.resources['course_dir'] = os.path.join(self.file_path, 'feedback_course')

    def test_zip_feedback(self):
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractFeedback().preprocess(path, resources)
        path, resources = CopyFeedback().preprocess(path, resources)
        path, resources = ZipFeedback().preprocess(path, resources)

        assert os.path.exists(path)
        assert os.path.isfile(os.path.join(path, 'multi_feedback.zip'))

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            rmtree(self.tmp_path) 

if __name__ == '__main__':
    unittest.main()