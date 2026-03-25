#main.py
#entry point for log file analyzer project 

def main():
    print("log file analyzer starting ...")


    analyzer = loganalyzer("logs/sample.log")
    analyzer.load()

    print("total log entries:",len(analyzer.entries))

    error_analyzer = ErrorLogAnalyzer("logs/sample.log")
    error_analyzer.load()

    print("Total error entries:", len(error_analyzer.get_errors()))

if __name__ == "__main__":
    main()