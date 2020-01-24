import unittest
import sys
import os
from shutil import rmtree
from ilias2nbgrader.preprocessors import Extract
from .base import TestsBase

class TestExtract(TestsBase):

    def test_paths(self):
        preprocessor = Extract()
        path, resources = preprocessor.preprocess(self.tmp_path, self.resources)


        assert os.path.exists(os.path.join(self.tmp_path, preprocessor.extract_path))
        for student in ['student1', 'student2', 'student3', 'student4']:
            assert os.path.exists(os.path.join(self.tmp_path, preprocessor.extract_path, student))

    def test_tmp_folders(self):
        preprocessor = Extract()
        self.resources['tmp_folders'] = set()
        path, resources = preprocessor.preprocess(self.tmp_path, self.resources)

        assert os.path.join(self.tmp_path, preprocessor.extract_path) in resources['tmp_folders']


    def tearDown(self):
        rmtree(self.tmp_path)

if __name__ == '__main__':
    unittest.main()


