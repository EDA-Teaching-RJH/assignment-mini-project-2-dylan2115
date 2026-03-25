import re 

#functions for regex extraction 

def extraxt_timestamp(line: str):
#this extracxts the time stamp from the sample log
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}
    match = re.search(pattern, line)
    return match.groupe(0) if match else none 

def extract_log_level(line: str):
#extracts the the type of error(info, warning and error)
    pattern = r"\b(info|warrning|error)\b"
    match = re.search(pattern,line)
    return match.group(0) if match else none

def extraxct_error_code(line:str):
#gives the code to the error 
    pattern = r"\b\d{3}\b"
    match = re.search(pattern, line)
    return match.group(0)if match else none 