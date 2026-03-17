"""Text processing utilities module.

This module provides common text processing functions for string manipulation
and analysis.
"""

import re
from typing import List


def count_words(text: str) -> int:
    """Count the number of words in a string.

    Words are defined as sequences of alphanumeric characters separated by
    whitespace.

    Args:
        text: The input string to count words from.

    Returns:
        The number of words in the input string. Returns 0 if the input
        is empty or contains only whitespace.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("  Multiple   spaces  ")
        2
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Strip leading/trailing whitespace and split on any whitespace
    words = text.strip().split()
    return len(words)


def count_sentences(text: str) -> int:
    """Count the number of sentences in a string.

    Sentences are identified by termination characters: period (.), 
    exclamation mark (!), or question mark (?).

    Args:
        text: The input string to count sentences from.

    Returns:
        The number of sentences in the input string. Returns 0 if the input
        is empty or contains no sentence terminators.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> count_sentences("Hello world. How are you?")
        2
        >>> count_sentences("Wow! Amazing. Really?")
        3
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text.strip():
        return 0
    
    # Count occurrences of sentence terminators
    sentences = re.findall(r'[.!?]+', text)
    return len(sentences)


def reverse_text(text: str) -> str:
    """Return the reversed version of the input string.

    Args:
        text: The input string to reverse.

    Returns:
        The reversed string.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> reverse_text("hello")
        'olleh'
        >>> reverse_text("123")
        '321'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return text[::-1]


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in the string.

    Args:
        text: The input string to capitalize.

    Returns:
        The string with the first letter of each word capitalized.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("multiple   spaces")
        'Multiple   Spaces'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return text.title()


def remove_extra_spaces(text: str) -> str:
    """Remove extra whitespace from the string.

    Replaces multiple consecutive spaces with a single space and strips
    leading and trailing whitespace.

    Args:
        text: The input string to process.

    Returns:
        The string with extra whitespace removed.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> remove_extra_spaces("  hello    world  ")
        'hello world'
        >>> remove_extra_spaces("multiple   spaces   here")
        'multiple spaces here'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Replace multiple spaces with single space and strip
    return ' '.join(text.split())
