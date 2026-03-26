# tests/test_analyzer.py
# Tests for the Log File Analyzer

from analyzer import LogAnalyzer, ErrorLogAnalyzer

def test_load_entries():
    analyzer = LogAnalyzer("Log_analyzer_project/logs/sample.log")
    analyzer.load()
    assert len(analyzer.entries) > 0

def test_count_by_ip():
    analyzer = LogAnalyzer("Log_analyzer_project/logs/sample.log")
    analyzer.load()
    counts = analyzer.count_by_ip()
    assert isinstance(counts,dict)
    assert all(isinstance(v, int) for v in counts.values())

def test_count_by_url():
    analyzer = LogAnalyzer("Log_analyzer_project/logs/sample.log")
    analyzer.load()
    counts = analyzer.count_by_url()
    assert isinstance(counts, dict)
    assert all(isinstance(v, int) for v in counts.values())
