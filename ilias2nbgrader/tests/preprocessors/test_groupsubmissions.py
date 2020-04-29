import unittest
import os
from shutil import rmtree
from .groupbase import TestsGroupBase
from ilias2nbgrader.preprocessors import Extract, ExtractAssignmentInfo, CreateFolderStructure, RenameSubmission, GroupSubmissions, RenameNotebooks

class TestGroupSubmissions(TestsGroupBase):

    def test_grouping_by_cell_id(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractAssignmentInfo().preprocess(path, resources)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        path, resources = RenameNotebooks().preprocess(path, resources)
        path, resources = RenameSubmission().preprocess(path, resources)
        path, resources = GroupSubmissions().preprocess(path, resources)

        for group in self.groups:
            assert os.path.exists(os.path.join(path, '_'.join(group)))

    def test_tmp_folder_does_not_exist(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractAssignmentInfo().preprocess(path, resources)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        path, resources = RenameNotebooks().preprocess(path, resources)
        path, resources = RenameSubmission().preprocess(path, resources)
        del resources['tmp_folders']
        path, resources = GroupSubmissions().preprocess(path, resources)        
        assert path in resources['tmp_folders']

    def test_no_grouping(self):
        del self.resources['group_cell']
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractAssignmentInfo().preprocess(path, resources)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        path, resources = RenameNotebooks().preprocess(path, resources)
        path, resources = RenameSubmission().preprocess(path, resources)
        path, resources = GroupSubmissions().preprocess(path, resources)

        for uid, student in self.submitted:
            assert os.path.exists(os.path.join(path, uid))

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            rmtree(self.tmp_path)

if __name__ == '__main__':
    unittest.main()