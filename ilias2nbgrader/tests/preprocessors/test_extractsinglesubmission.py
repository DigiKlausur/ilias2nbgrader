import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import ExtractAssignmentInfo, Extract, ExtractSingleSubmission


class TestExtractSingleSubmission(TestsBase):

    def setUp(self):
        super().setUp()
        self.resources['submission_zip'] = os.path.join(self.file_path, 'zipped_submissions.zip')

    def test_student1(self):
        '''
        Zipped folder with submission inside

        submission.zip
        └── some_folder
            └── problem_set_oneeeee.ipynb
        '''
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = Extract().preprocess(path, resources)        
        path, resources = ExtractSingleSubmission().preprocess(path, resources)
        assert os.path.exists(os.path.join(path, 'student1'))
        assert os.path.isfile(os.path.join(path, 'student1', 'problem_set_oneeeee.ipynb'))

    def test_student2(self):
        '''
        Single notebook inside

        problem_set_one.ipynb
        '''
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = Extract().preprocess(path, resources)        
        path, resources = ExtractSingleSubmission().preprocess(path, resources)
        assert os.path.exists(os.path.join(path, 'student2'))
        assert os.path.isfile(os.path.join(path, 'student2', 'problem_set_one.ipynb'))

    def test_student3(self):
        '''
        Folder with a mix of zip and other files
        
        problem_set_one.ipynb
        problem_set_two.ipynb.zip
        '''
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = Extract().preprocess(path, resources)        
        path, resources = ExtractSingleSubmission().preprocess(path, resources)
        assert os.path.exists(os.path.join(path, 'student3'))
        assert os.path.isfile(os.path.join(path, 'student3', 'problem_set_one.ipynb'))
        assert os.path.isfile(os.path.join(path, 'student3', 'problem_set_two.ipynb.zip'))

    def test_student4(self):
        '''
        Zipped folder with submission inside

        submission.zip
        └── nested_folder
            ├── problem_set_one_1.ipynb
            └── nested_subfolder
                └── ps2.ipynb
        '''
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = Extract().preprocess(path, resources)        
        path, resources = ExtractSingleSubmission().preprocess(path, resources)
        assert os.path.exists(os.path.join(path, 'student4'))
        assert os.path.isfile(os.path.join(path, 'student4', 'problem_set_one_1.ipynb'))
        assert os.path.isdir(os.path.join(path, 'student4', 'nested_subfolder'))
        assert os.path.isfile(os.path.join(path, 'student4', 'nested_subfolder', 'ps2.ipynb'))

    def test_student5(self):
        '''
        Zipped folder with single file inside

        singlefile.zip
        └── a
            └── b
                ├── some_file.txt
                └── c
        '''
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = Extract().preprocess(path, resources)        
        path, resources = ExtractSingleSubmission().preprocess(path, resources)
        assert os.path.exists(os.path.join(path, 'student5'))
        assert os.path.isfile(os.path.join(path, 'student5', 'some_file.txt'))
        assert not os.path.exists(os.path.join(path, 'student5', 'c'))

    def test_tmp_folders(self):
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = Extract().preprocess(path, resources)        
        path, resources = ExtractSingleSubmission().preprocess(path, resources)
        assert os.path.join(self.tmp_path, ExtractSingleSubmission().directory) in resources['tmp_folders']

    def tearDown(self):
        rmtree(self.tmp_path)

if __name__ == '__main__':
    unittest.main()



