import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import Extract


class TestExtract(TestsBase):

    def test_paths(self):
        preprocessor = Extract()
        path, resources = preprocessor.preprocess(self.tmp_path, self.resources)


        assert os.path.exists(os.path.join(self.tmp_path, preprocessor.extract_path))
        for student in self.students:
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


