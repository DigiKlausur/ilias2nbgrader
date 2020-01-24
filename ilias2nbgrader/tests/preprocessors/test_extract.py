import unittest
import sys
import os
from shutil import rmtree
from ilias2nbgrader.preprocessors import Extract

class TestExtract(unittest.TestCase):

    def setUp(self):
        self.base_path = os.path.normpath('ilias2nbgrader/tests/preprocessors')
        self.file_path = os.path.join(self.base_path, 'files')
        self.course_dir = os.path.join(self.file_path, 'test_course')
        self.resources = {
            'course_dir': self.course_dir,
            'assignment': 'assignment_one',
            'path': 'tmp',
            'submission_zip': os.path.join(self.file_path, 'submissions.zip')
        }

    def test_paths(self):
        preprocessor = Extract()
        path, resources = preprocessor.preprocess('tmp', self.resources)

        assert os.path.exists('tmp/extracted')
        assert os.path.exists('tmp/extracted/student1')
        assert os.path.exists('tmp/extracted/student2')
        assert os.path.exists('tmp/extracted/student3')
        assert os.path.exists('tmp/extracted/student4')

    def test_tmp_folders(self):
        preprocessor = Extract()
        self.resources['tmp_folders'] = set()
        path, resources = preprocessor.preprocess('tmp', self.resources)

        assert 'tmp/extracted' in resources['tmp_folders']


    def tearDown(self):
        rmtree('tmp')

if __name__ == '__main__':
    unittest.main()


