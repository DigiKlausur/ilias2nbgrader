import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import Extract, ExtractAssignmentInfo, CreateFolderStructure, AddExtraFiles

class TestAddExtraFiles(TestsBase):

    def test_no_extra_files(self):
        preprocessor = AddExtraFiles()
        path, resources = preprocessor.preprocess('', self.resources)

        assert 'extra_files' not in resources
        assert resources['path'] == self.tmp_path

    def test_extra_files(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractAssignmentInfo().preprocess(path, resources)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        path, resources = AddExtraFiles().preprocess(path, resources)
        
        assert os.path.exists(path)

        for student in self.students:
            assert os.path.exists(os.path.join(path, student))
            assert os.path.exists(os.path.join(path, student, self.assignment, 'data'))
            assert os.path.isfile(os.path.join(path, student, self.assignment, 'data', 'file.txt'))

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            rmtree(self.tmp_path)

if __name__ == '__main__':
    unittest.main()