import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import Extract, CreateFolderStructure, MoveToSubmitted, DeleteTempFolders

class TestDeleteTempFolders(TestsBase):

    def test_delete_nothing(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        extract_path = path
        assert os.path.exists(extract_path)
        path, resources = DeleteTempFolders().preprocess(path, resources)
        assert os.path.exists(extract_path)

    def test_delete_partial(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        extract_path = path
        assert os.path.exists(extract_path)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        restructured_path = path
        assert os.path.exists(path)
        path, resources = DeleteTempFolders().preprocess(path, resources)
        assert not os.path.exists(extract_path)
        assert os.path.exists(restructured_path)

    def test_delete_full_tmp(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        print(path)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        print(path)
        path, resources = MoveToSubmitted().preprocess(path, resources)
        print(path)
        path, resources = DeleteTempFolders().preprocess(path, resources)
        assert not os.path.exists(self.tmp_path)

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            rmtree(self.tmp_path)
        if os.path.exists(os.path.join(self.course_dir, 'submitted')):
            rmtree(os.path.join(self.course_dir, 'submitted'))
            
if __name__ == '__main__':
    unittest.main()