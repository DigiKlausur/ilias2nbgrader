import unittest
import sys
from ...preprocessors import ExtractAssignmentInfo

class TestExtractAssignmentInfo(unittest.TestCase):

    def setUp(self):
        self.resources = {
            'course_dir': 'ilias2nbgrader/tests/preprocessors/files/test_course',
            'assignment': 'assignment_one',
            'path': 'tmp',
            'submission_zip': 'files/submissions.zip'
        }

    def test_source_notebooks(self):
        preprocessor = ExtractAssignmentInfo()
        path, resources = preprocessor.preprocess('', self.resources)

        assert 'source_notebooks' in resources
        assert 'problem_set_one.ipynb' in resources['source_notebooks'] 
        assert len(resources['source_notebooks']) == 1

    def test_extra_files(self):
        preprocessor = ExtractAssignmentInfo()
        path, resources = preprocessor.preprocess('', self.resources)
        print(resources)

        assert 'extra_files' in resources
        assert 'base_path' in resources['extra_files']
        assert 'files' in resources['extra_files']
        assert resources['extra_files']['base_path'] == 'ilias2nbgrader/tests/preprocessors/files/test_course/source/assignment_one'
        assert len(resources['extra_files']['files']) == 1
        assert 'data/file.txt' in resources['extra_files']['files']

if __name__ == '__main__':
    unittest.main()


