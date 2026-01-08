"""Tests for utils module."""

import pytest

from src.utils import add, divide, format_version, greet, multiply


class TestGreet:
    """Tests for greet function."""

    def test_greet_returns_message(self):
        result = greet("World")
        assert result == "Hello, World! Welcome to the organization template."

    def test_greet_with_empty_string_raises_error(self):
        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            greet("")

    def test_greet_with_none_raises_error(self):
        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            greet(None)


class TestAdd:
    """Tests for add function."""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestMultiply:
    """Tests for multiply function."""

    def test_multiply_positive_numbers(self):
        assert multiply(2, 3) == 6

    def test_multiply_with_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    """Tests for divide function."""

    def test_divide_normal(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(10, 0)


class TestFormatVersion:
    """Tests for format_version function."""

    def test_format_version(self):
        assert format_version(1, 2, 3) == "v1.2.3"

    def test_format_version_zeros(self):
        assert format_version(0, 0, 0) == "v0.0.0"
