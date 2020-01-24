import unittest
import os
from .base import TestsBase
from ilias2nbgrader.preprocessors import ExtractAssignmentInfo

class TestExtractAssignmentInfo(TestsBase):

    def test_source_notebooks(self):
        preprocessor = ExtractAssignmentInfo()
        path, resources = preprocessor.preprocess('', self.resources)

        assert 'source_notebooks' in resources
        assert 'problem_set_one.ipynb' in resources['source_notebooks'] 
        assert len(resources['source_notebooks']) == 1

    def test_extra_files(self):
        preprocessor = ExtractAssignmentInfo()
        path, resources = preprocessor.preprocess('', self.resources)

        assert 'extra_files' in resources
        assert 'base_path' in resources['extra_files']
        assert 'files' in resources['extra_files']
        assert resources['extra_files']['base_path'] == os.path.join(self.course_dir, 'source', self.assignment)
        assert len(resources['extra_files']['files']) == 1
        assert 'data/file.txt' in resources['extra_files']['files']

if __name__ == '__main__':
    unittest.main()