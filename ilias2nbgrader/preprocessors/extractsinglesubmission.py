import glob
import os
import zipfile
from traitlets import Unicode
from .preprocessor import Preprocessor
from ..utils import copyfiles


class ExtractSingleSubmission(Preprocessor):

    directory = Unicode('unzipped', help='Subfolder where processed files go')

    def __init__(self):
        super(ExtractSingleSubmission, self).__init__()

    def preprocess_student(self, student, resources):
        # Check if submission is a single archive
        submitted_files = []
        for root, _, files in os.walk(os.path.join(self.src, student)):
            for file in files:
                submitted_files.append(os.path.join(root, file))

        if len(submitted_files) == 1 and submitted_files[0].endswith('.zip'):
            # Found single zip

            with zipfile.ZipFile(submitted_files[0], 'r') as zip_ref:
                zip_ref.extractall(self.dst)

        else:
            copyfiles(self.src, self.dst)

        return student, resources