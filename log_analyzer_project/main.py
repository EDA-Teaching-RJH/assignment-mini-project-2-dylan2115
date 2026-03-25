#main.py
#entry point for log file analyzer project
from analyzer import LogAnalyzer, ErrorLogAnalyzer
#impoerts the classes 

def main():
    print("log file analyzer starting ...")
# Create a LogAnalyzer for the sample log file


    analyzer = LogAnalyzer("logs/sample.log")
    analyzer.load()
#loads the files 
    print("total log entries:",len(analyzer.entries))
#prints total files 
# Create an ErrorLogAnalyzer for the same file
    error_analyzer = ErrorLogAnalyzer("logs/sample.log")
    error_analyzer.load()
#loads errors only 
    print("Total error entries:", len(error_analyzer.get_errors()))

if __name__ == "__main__":
    main()