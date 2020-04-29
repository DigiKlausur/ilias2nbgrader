import unittest
import os

class TestsGroupBase(unittest.TestCase):


    def setUp(self):
        self.base_path = os.path.normpath('ilias2nbgrader/tests/preprocessors')
        self.file_path = os.path.join(self.base_path, 'files')
        self.course_dir = os.path.join(self.file_path, 'group_course')
        self.assignment = 'assignment_one'
        self.tmp_path = 'tmp'
        self.students = [('jdoe12s', 'Doe_Jane_jdoe12s_2345678'),
                         ('jdoe2s', 'Doe_John_jdoe2s_1234567'),
                         ('fdoe2s', 'Doey_Fred_fdoe2s_7654321'),
                         ('ppark2s', 'Parker_Peter_ppark2s_0123456'),
                         ('msue2s', 'Sue_Mary_msue2s_3456789'),
                         ('etux2s', 'Tux_Edo_etux2s_4567890'),
                         ('nnote2s', 'Norbert_Notebookless_nnote2s_876543'),
                         ('snosub2s', 'Susy_Nosubmission_snosub2s_6543210')]
        self.feedback = [('jdoe12s', 'Doe_Jane_jdoe12s_2345678'),
                         ('jdoe2s', 'Doe_John_jdoe2s_1234567'),
                         ('fdoe2s', 'Doey_Fred_fdoe2s_7654321'),
                         ('ppark2s', 'Parker_Peter_ppark2s_0123456'),
                         ('msue2s', 'Sue_Mary_msue2s_3456789'),
                         ('etux2s', 'Tux_Edo_etux2s_4567890')]
        self.groups = [('jdoe12s', ),
                       ('fdoe2s', 'jdoe2s'),
                       ('ppark2s', ),
                       ('etux2s', 'msue2s'),
                       ('nnote2s', )]
        self.submitted = [('jdoe12s', 'Doe_Jane_jdoe12s_2345678'),
                         ('jdoe2s', 'Doe_John_jdoe2s_1234567'),
                         ('ppark2s', 'Parker_Peter_ppark2s_0123456'),
                         ('msue2s', 'Sue_Mary_msue2s_3456789'),
                         ('etux2s', 'Tux_Edo_etux2s_4567890'),
                         ('nnote2s', 'Norbert_Notebookless_nnote2s')]
        
        self.resources = {
            'course_dir': self.course_dir,
            'assignment': self.assignment,
            'path': self.tmp_path,
            'group_cell': 1,
            'submission_zip': os.path.join(self.file_path, 'group_submissions.zip'),
            'feedback_zip': os.path.join(self.file_path, 'group_feedback.zip')
        }