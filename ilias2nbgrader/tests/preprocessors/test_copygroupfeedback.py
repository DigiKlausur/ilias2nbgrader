import unittest
import os
from shutil import rmtree
from .groupbase import TestsGroupBase
from ilias2nbgrader.preprocessors import ExtractAssignmentInfo, ExtractFeedback, CopyGroupFeedback

class TestCopyGroupFeedback(TestsGroupBase):

    def setUp(self):
        super().setUp()

    def test_copy_feedback(self):
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractFeedback().preprocess(path, resources)
        path, resources = CopyGroupFeedback().preprocess(path, resources)
        assert os.path.exists(self.tmp_path)
        for uid, student in self.feedback:
            print(uid)
            assert os.path.exists(os.path.join(path, student))
            assert os.path.isfile(os.path.join(path, student, 'problem_set_one.html'))
        assert os.path.exists(os.path.join(path, 'Norbert_Notebookless_nnote2s_876543'))
        assert not os.path.isfile(os.path.join(path, 'Norbert_Notebookless_nnote2s_876543', 'problem_set_one.html'))
        assert os.path.exists(os.path.join(path, 'Susy_Nosubmission_snosub2s_6543210'))
        assert not os.path.isfile(os.path.join(path, 'Susy_Nosubmission_snosub2s_6543210', 'problem_set_one.html'))

    def test_tmp_folder_does_not_exist(self):
        path, resources = ExtractAssignmentInfo().preprocess(self.tmp_path, self.resources)
        path, resources = ExtractFeedback().preprocess(path, resources)
        del resources['tmp_folders']
        path, resources = CopyGroupFeedback().preprocess(path, resources)
        assert path in resources['tmp_folders']

    def tearDown(self):
        if os.path.exists(self.tmp_path):
            rmtree(self.tmp_path) 

if __name__ == '__main__':
    unittest.main()