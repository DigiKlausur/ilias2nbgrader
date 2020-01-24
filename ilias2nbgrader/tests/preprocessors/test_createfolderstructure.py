import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import Extract, CreateFolderStructure


class TestCreateFolderStructure(TestsBase):

    def test_paths(self):
        preprocessor = Extract()
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = CreateFolderStructure().preprocess(path, resources)

        assert os.path.exists(os.path.join(self.tmp_path, CreateFolderStructure().directory))

        for student in self.students:
            assert os.path.exists(os.path.join(self.tmp_path, CreateFolderStructure().directory, student, self.assignment))

    def tearDown(self):
        rmtree(self.tmp_path)

if __name__ == '__main__':
    unittest.main