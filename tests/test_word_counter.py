"""Tests for word_counter.py"""
import os
import tempfile
from word_counter import count_stats


def test_count_stats():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Hello World\nThis is a test\n")
        f.flush()
        stats = count_stats(f.name)
    os.unlink(f.name)
    assert stats["lines"] == 2
    assert stats["words"] == 6
    assert stats["characters"] == 26
