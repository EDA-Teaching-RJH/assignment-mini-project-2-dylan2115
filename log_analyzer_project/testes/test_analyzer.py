# tests/test_analyzer.py
# Tests for the Log File Analyzer

from analyzer import LogAnalyzer, ErrorLogAnalyzer

def test_load_entries():
    analyzer = LogAnalyzer("Log_analyzer_project/logs/sample.log")
    analyzer.load()
    assert len(analyzer.entries) > 0

