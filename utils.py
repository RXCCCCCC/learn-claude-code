"""Utility functions module.

This module provides common utility functions for mathematical operations
and string manipulation.
"""

from typing import List


def add(a: int, b: int) -> int:
    """Add two integers together.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The sum of a and b.

    Examples:
        >>> add(2, 3)
        5
    """
    return a + b


def greet(name: str) -> str:
    """Generate a greeting message for a given name.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.

    Examples:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def sum_list(numbers: List[int]) -> int:
    """Calculate the sum of a list of integers.

    Args:
        numbers: A list of integers to sum.

    Returns:
        The sum of all integers in the list.

    Examples:
        >>> sum_list([1, 2, 3, 4])
        10
    """
    return sum(numbers)
