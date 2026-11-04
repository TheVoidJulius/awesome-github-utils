"""Tests for password_generator.py"""
from password_generator import generate_password


def test_password_length():
    pwd = generate_password(length=20)
    assert len(pwd) == 20


def test_password_no_special():
    pwd = generate_password(length=100, use_special=False)
    assert pwd.isalnum()


def test_password_uniqueness():
    passwords = {generate_password() for _ in range(10)}
    assert len(passwords) == 10  # All should be unique
