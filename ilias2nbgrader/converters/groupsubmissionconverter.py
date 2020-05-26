from traitlets.config import LoggingConfigurable, Config
from traitlets import List, Unicode
from .converter import Converter
from ..preprocessors import *

class GroupSubmissionConverter(Converter):
    
    preprocessors = List([
        ExtractAssignmentInfo,
        Extract,
        ExtractSingleSubmission,
        CreateFolderStructure,
        RenameNotebooks,
        AddExtraFiles,
        RestructureSubmission,
        RenameSubmission,
        GroupSubmissions,
        MoveToSubmitted,
        DeleteTempFolders
    ], help='List of preprocessors for the converter')
    
    def __init__(self, config=None):
        super(GroupSubmissionConverter, self).__init__(config=config)