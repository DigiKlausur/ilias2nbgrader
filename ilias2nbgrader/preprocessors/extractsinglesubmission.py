import glob
import os
import zipfile
from traitlets import Unicode
from .preprocessor import Preprocessor
from ..utils import movefiles
import os

class ExtractSingleSubmission(Preprocessor):

    directory = Unicode('unzipped', help='Subfolder where processed files go')

    def __init__(self):
        super(ExtractSingleSubmission, self).__init__()

    def strip_prefix(self, zipinfo):
        prefix = os.path.commonprefix([os.path.split(info.filename)[0] for info in zipinfo])
        for info in zipinfo:
            info.filename = os.path.relpath(info.filename, prefix)
        return zipinfo

    def preprocess_student(self, student, resources):
        self.init_logging('Unzip Submission')
        src = os.path.join(self.src, student)
        dst = os.path.join(self.dst, student)

        # Check if submission is a single archive
        zips = []
        other = []
        for root, _, files in os.walk(src):
            for file in files:
                if file.endswith('.zip'):
                    zips.append(os.path.join(root, file))
                else:
                    other.append(os.path.join(root, file))

        if len(other) < 1:
            # Only archives or no files found
            for archive in zips:
                with zipfile.ZipFile(archive, 'r') as zip_ref:
                    zipinfo = self.strip_prefix([info for info in zip_ref.infolist() \
                        if not info.filename.endswith(os.path.sep)])
                    zip_ref.extractall(dst, members=zipinfo)
                self.log.info('{}: Extract zip {}'.format(student, file))
        else:
            movefiles(src, dst)

        self.terminate_logging(os.path.join(dst, self.logname))

        return student, resources