import unittest
import os
from shutil import rmtree
from .groupbase import TestsGroupBase
from ilias2nbgrader.preprocessors import Extract, ExtractAssignmentInfo, CreateFolderStructure, RenameSubmission

class TestRenameSubmission(TestsGroupBase):

    def test_rename(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractAssignmentInfo().preprocess(path, resources)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        path, resources = RenameSubmission().preprocess(path, resources)

        for uid, student in self.submitted:
            assert os.path.exists(os.path.join(path, uid))

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            rmtree(self.tmp_path)

if __name__ == '__main__':
    unittest.main()