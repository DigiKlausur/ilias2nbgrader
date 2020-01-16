from traitlets.config import LoggingConfigurable, Config
from traitlets import List, Unicode
from traitlets.utils.importstring import import_item
from .converter import Converter
from ..preprocessors import *

class SubmissionConverter(Converter):
    
    preprocessors = List([
        ExtractAssignmentInfo,
        Extract,
        CreateFolderStructure,
        RenameNotebooks,
        AddExtraFiles,
        RestructureSubmission,
        MoveToSubmitted,
        DeleteTempFolders
    ], help='List of preprocessors for the converter')
    
    def __init__(self, config=None):
        super(SubmissionConverter, self).__init__(config=config)