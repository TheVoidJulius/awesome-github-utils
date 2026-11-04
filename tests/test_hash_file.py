"""Tests for hash_file.py"""
import os
import tempfile
from hash_file import hash_file


def test_sha256():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("test content")
        f.flush()
        result = hash_file(f.name, "sha256")
    os.unlink(f.name)
    assert len(result) == 64  # SHA256 hex length


def test_md5():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("test content")
        f.flush()
        result = hash_file(f.name, "md5")
    os.unlink(f.name)
    assert len(result) == 32  # MD5 hex length
