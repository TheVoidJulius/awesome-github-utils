"""Tests for json_formatter.py"""
from json_formatter import format_json


def test_format_simple():
    result = format_json('{"b":1,"a":2}')
    assert '"a": 2' in result
    assert '"b": 1' in result


def test_format_nested():
    result = format_json('{"outer":{"inner":true}}')
    assert "inner" in result


def test_format_indent():
    result = format_json('{"key":"val"}', indent=4)
    assert '    "key"' in result
