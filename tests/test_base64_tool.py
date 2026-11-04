"""Tests for base64_tool.py"""
from base64_tool import encode, decode


def test_encode():
    assert encode("Hello") == "SGVsbG8="


def test_decode():
    assert decode("SGVsbG8=") == "Hello"


def test_roundtrip():
    original = "The quick brown fox"
    assert decode(encode(original)) == original
