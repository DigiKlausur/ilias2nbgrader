import os
import io
import logging
from traitlets.config import LoggingConfigurable
from traitlets import Unicode

class Preprocessor(LoggingConfigurable):
    
    src = Unicode('', help='Source path to read from')
    dst = Unicode('', help='Destination path to write to')
    logname = Unicode('converter.log', help='Name of the logfile')
    
    def __init__(self):
        self.log_handlers = []
    
    def init_logging(self, name):
        self.log_buff = io.StringIO()
        handler = logging.StreamHandler(self.log_buff)        
        formatter = logging.Formatter(fmt="[{} %(levelname)s] %(message)s".format(name))
        handler.setFormatter(formatter)
        self.log.setLevel(logging.INFO)
        self.log.addHandler(handler)
        self.log_handlers.append(handler)
        
    def terminate_logging(self, logfile):
        for handler in self.log_handlers:
            self.log.removeHandler(handler)
        if self.log_buff:
            with open(logfile, 'a') as f_log:
                f_log.write(self.log_buff.getvalue()) 
    
    def preprocess_student(self, student, resources):
        raise NotImplementedError('should be implemented by subclass')
        return student, resources
        
    def preprocess(self, path, resources):
        raise NotImplementedError('should be implemented by subclass')
        return path, resources
