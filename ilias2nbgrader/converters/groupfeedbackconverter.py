from traitlets.config import LoggingConfigurable, Config
from traitlets import List, Unicode
from .converter import Converter
from ..preprocessors import *

class GroupFeedbackConverter(Converter):
    
    preprocessors = List([
        ExtractAssignmentInfo,
        ExtractFeedback,
        CopyGroupFeedback,
        ZipFeedback,
        DeleteTempFolders
    ], help='List of preprocessors for the converter')
    
    def __init__(self, config=None):
        super(GroupFeedbackConverter, self).__init__(config=config)