#main.py
#entry point for log file analyzer project
from .analyzer import LogAnalyzer, ErrorLogAnalyzer
#impoerts the classes 

def main():
    import inspect
    
    print("=" * 20)
    print("Initializing Log File Analyzer...",flush=True)
    print("=" * 20)
# Create a LogAnalyzer for the sample log file


    analyzer = LogAnalyzer("log_analyzer_project/logs/sample.log")
    analyzer.load()
#loads the files 
    print("Total log entries:",len(analyzer.entries))
#prints total files 
# Create an ErrorLogAnalyzer for the same file
    error_analyzer = ErrorLogAnalyzer("log_analyzer_project/logs/sample.log")
    error_analyzer.load()
#loads errors only 
    print("Total error entries:", len(error_analyzer.get_errors()))

    ip_counts = analyzer.count_by_ip()
    print("\nRequests per IP:")
    for ip, count in ip_counts.items():
        print(f"   {ip}: {count}")
#count requests per ip

    url_counts = analyzer.count_by_url()
    print("\nRequests per URL:")
    for url, count in url_counts.items():
        print(f"   {url}: {count}")
#counts requests per url

    error_code_counts = error_analyzer.count_by_error_code()
    print("\nErrors by code:")
    for code, count in error_code_counts.items():
        print(f"   {code}: {count}")
#counts requests errorcode 
    print("=" * 20)
    print("Analysis complete")
    print("=" * 20)

    if __name__ == "__main__":
        main()