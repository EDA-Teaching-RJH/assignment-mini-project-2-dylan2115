# analyzer 
#classes for parsing and analyzing log files 

from utils import (
    extract_timestamp,
    extract_log_level,
    extract_error_code,
    extract_ip,
    extract_url
)

class LogEntry:
    def __init__(self, line: str):
        self.raw = line
        self.timestamp = extract_timestamp(line)
        self.log_level = extract_log_level(line)
        self.error_code = extract_error_code(line)
        self.ip = extract_ip(line)
        self.url = extract_url(line)

    def __repr__(self):
        return f"<LogEntry {self.timestamp} {self.log_level} {self.ip}>"
#this class shows one line from the sample log 
#it stores all the values from timestamp to the url 
    
class LogAnalyzer:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.entries= []

    def load(self):
        with open(self.filepath, "r") as f:
            for line in f:
                entry = LogEntry(line.strip())
                self.entries.append(entry)
#loads the log and creates a list of LogEntry objects 

class ErrorLogAnalyzer(LogAnalyzer):
    def get_errors(self):
        return [e for e in self.entries if e.log_level == "ERROR"]
#this class focuses on errors