import re 

#functions for regex extraction 

def extraxt_timestamp(line: str):
#this extracxts the time stamp from the sample log
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}
    match = re.search(pattern, line)
    return match.groupe(0) if match else none 

