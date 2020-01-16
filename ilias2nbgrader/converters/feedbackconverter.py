from traitlets.config import LoggingConfigurable, Config
from traitlets import List, Unicode
from traitlets.utils.importstring import import_item
from .converter import Converter
from ..preprocessors import *

class FeedbackConverter(Converter):
    
    preprocessors = List([
        ExtractAssignmentInfo,
        ExtractFeedback,
        CopyFeedback,
        ZipFeedback,
        DeleteTempFolders
    ], help='List of preprocessors for the converter')
    
    def __init__(self, config=None):
        super(FeedbackConverter, self).__init__(config=config)