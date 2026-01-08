"""
Demo module for the organization template.

This is a sample file to demonstrate CI/CD workflows with Python.
"""


def greet(name: str) -> str:
    """
    Greet a user with a welcome message.

    Args:
        name: The name to greet.

    Returns:
        The greeting message.

    Raises:
        ValueError: If name is empty or not a string.
    """
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string")
    return f"Hello, {name}! Welcome to the organization template."


def add(a: float, b: float) -> float:
    """
    Calculate the sum of two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide two numbers.

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        The quotient of a and b.

    Raises:
        ZeroDivisionError: When divisor is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def format_version(major: int, minor: int, patch: int) -> str:
    """
    Format a semantic version string.

    Args:
        major: Major version number.
        minor: Minor version number.
        patch: Patch version number.

    Returns:
        Formatted version string (e.g., 'v1.2.3').
    """
    return f"v{major}.{minor}.{patch}"
