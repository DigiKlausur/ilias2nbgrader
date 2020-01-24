import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import Extract, ExtractAssignmentInfo, CreateFolderStructure, RenameNotebooks

class TestRenameNotebooks(TestsBase):

    def test_rename(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractAssignmentInfo().preprocess(path, resources)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        path, resources = RenameNotebooks().preprocess(path, resources)

        for student in self.students:
            assert os.path.exists(os.path.join(path, student))
            for src_nb in resources['source_notebooks']:
                assert os.path.isfile(os.path.join(path, student, self.assignment, src_nb))

    def test_other(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractAssignmentInfo().preprocess(path, resources)
        path, resources = CreateFolderStructure().preprocess(path, resources)
        path, resources = RenameNotebooks().preprocess(path, resources)

        assert os.path.isfile(os.path.join(path, 'student3', self.assignment, 'problem_set_two.ipynb'))
        assert os.path.isfile(os.path.join(path, 'student4', self.assignment, 'ps2.ipynb'))
        assert not os.path.isfile(os.path.join(path, 'student5', self.assignment, 'problem_set_one.ipynb'))

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            rmtree(self.tmp_path)

if __name__ == '__main__':
    unittest.main()