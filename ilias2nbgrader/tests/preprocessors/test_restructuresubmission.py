import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import Extract, ExtractAssignmentInfo, CreateFolderStructure, AddExtraFiles, RenameNotebooks, RestructureSubmission

class TestRestructureSubmission(TestsBase):

    def test_rename(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractAssignmentInfo().preprocess(path, resources)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        path, resources = AddExtraFiles().preprocess(path, resources)
        path, resources = RenameNotebooks().preprocess(path, resources)
        path, resources = RestructureSubmission().preprocess(path, resources)

        assert os.path.exists(path)
        assert os.path.isfile(os.path.join(self.tmp_path, RestructureSubmission().directory, 'student2', self.assignment, 'file.txt'))

        

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            #rmtree(self.tmp_path)
            pass

if __name__ == '__main__':
    unittest.main()