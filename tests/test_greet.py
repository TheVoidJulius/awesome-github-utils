"""Tests for greet.py"""
from greet import greet


def test_greet_default():
    assert greet("World") == "Hello, World! 👋"


def test_greet_custom_name():
    assert greet("Alice") == "Hello, Alice! 👋"


def test_greet_empty():
    assert greet("") == "Hello, ! 👋"
