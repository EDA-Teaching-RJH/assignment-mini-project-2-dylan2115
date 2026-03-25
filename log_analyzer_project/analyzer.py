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