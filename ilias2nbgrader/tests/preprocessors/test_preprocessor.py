import unittest
import os
from shutil import rmtree
from .base import TestsBase
from ilias2nbgrader.preprocessors import Preprocessor


class TestPreprocessor(TestsBase):

    def test_process_student(self):
        preprocessor = Preprocessor()
        student = 'student1'
        stud, resources = preprocessor.preprocess_student(student, self.resources)
        assert student == stud
        assert self.resources == resources

if __name__ == '__main__':
    unittest.main()


