import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import Extract, MoveToSubmitted

class TestMoveToSubmitted(TestsBase):

    def test_submitted(self):
        path, resources = Extract().preprocess(self.tmp_path, self.resources)
        path, resources = MoveToSubmitted().preprocess(path, resources)
        
        assert os.path.exists(path)
        assert os.path.normpath(path) == os.path.normpath(os.path.join(self.course_dir, 'submitted'))

        for student in self.students:
            assert os.path.exists(os.path.join(path, student))
            for root, _, files in os.walk(os.path.join(self.tmp_path, Extract().extract_path, student)):
                for file in files:
                    rel_path = os.path.relpath(os.path.join(root, file), start=os.path.join(self.tmp_path, Extract().extract_path))
                    assert os.path.isfile(os.path.join(path, rel_path))

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            rmtree(self.tmp_path)
        if os.path.exists(os.path.join(self.course_dir, 'submitted')):
            rmtree(os.path.join(self.course_dir, 'submitted'))

if __name__ == '__main__':
    unittest.main()