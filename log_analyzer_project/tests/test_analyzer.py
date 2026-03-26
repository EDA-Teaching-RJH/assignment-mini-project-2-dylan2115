# tests/test_analyzer.py
# Tests for the Log File Analyzer

from log_analyzer_project.analyzer import LogAnalyzer, ErrorLogAnalyzer


def test_load_entries():
    analyzer = LogAnalyzer("log_analyzer_project/logs/sample.log")
    analyzer.load()
    assert len(analyzer.entries) > 0

def test_count_by_ip():
    analyzer = LogAnalyzer("log_analyzer_project/logs/sample.log")
    analyzer.load()
    counts = analyzer.count_by_ip()
    assert isinstance(counts,dict)
    assert all(isinstance(v, int) for v in counts.values())

def test_count_by_url():
    analyzer = LogAnalyzer("log_analyzer_project/logs/sample.log")
    analyzer.load()
    counts = analyzer.count_by_url()
    assert isinstance(counts, dict)
    assert all(isinstance(v, int) for v in counts.values())

def test_error_entries():
    error_analyzer = ErrorLogAnalyzer("log_analyzer_project/logs/sample.log")
    error_analyzer.load()
    errors = error_analyzer.get_errors()
    assert len(errors) > 0

def test_error_code_counts():
    error_analyzer = ErrorLogAnalyzer("log_analyzer_project/logs/sample.log")
    error_analyzer.load()
    counts = error_analyzer.count_by_error_code()
    assert isinstance(counts, dict)
    assert all(isinstance(v, int) for v in counts.values())
