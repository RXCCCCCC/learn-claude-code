"""Test script for text_processor module.

This script tests all functions in the text_processor module to ensure
they work correctly.
"""

from text_processor import (
    count_words,
    count_sentences,
    reverse_text,
    capitalize_words,
    remove_extra_spaces
)


def test_all_functions():
    """Test all functions in the text_processor module."""
    
    print("=" * 60)
    print("Testing text_processor module")
    print("=" * 60)
    
    # Test count_words
    print("\n1. Testing count_words()")
    print("-" * 40)
    
    test_cases_words = [
        ("Hello world", 2),
        ("", 0),
        ("   ", 0),
        ("One", 1),
        ("  Multiple   spaces  here  ", 3),
        ("Testing with numbers 123 and symbols !@#", 7)
    ]
    
    for text, expected in test_cases_words:
        result = count_words(text)
        status = "[PASS]" if result == expected else "[FAIL]"
        print(f"{status} count_words('{text}') = {result} (expected {expected})")
    
    # Test count_sentences
    print("\n2. Testing count_sentences()")
    print("-" * 40)
    
    test_cases_sentences = [
        ("Hello world. How are you?", 2),
        ("", 0),
        ("No punctuation here", 0),
        ("Wow! Amazing. Really?", 3),
        ("One sentence.", 1),
        ("Multiple!!! Questions??? Yes.", 3)
    ]
    
    for text, expected in test_cases_sentences:
        result = count_sentences(text)
        status = "[PASS]" if result == expected else "[FAIL]"
        print(f"{status} count_sentences('{text}') = {result} (expected {expected})")
    
    # Test reverse_text
    print("\n3. Testing reverse_text()")
    print("-" * 40)
    
    test_cases_reverse = [
        ("hello", "olleh"),
        ("", ""),
        ("a", "a"),
        ("123", "321"),
        ("racecar", "racecar"),
        ("Hello World!", "!dlroW olleH")
    ]
    
    for text, expected in test_cases_reverse:
        result = reverse_text(text)
        status = "[PASS]" if result == expected else "[FAIL]"
        print(f"{status} reverse_text('{text}') = '{result}' (expected '{expected}')")
    
    # Test capitalize_words
    print("\n4. Testing capitalize_words()")
    print("-" * 40)
    
    test_cases_capitalize = [
        ("hello world", "Hello World"),
        ("", ""),
        ("already Capitalized", "Already Capitalized"),
        ("multiple   spaces", "Multiple   Spaces"),
        ("ALL CAPS", "All Caps"),
        ("123 numbers 456", "123 Numbers 456")
    ]
    
    for text, expected in test_cases_capitalize:
        result = capitalize_words(text)
        status = "[PASS]" if result == expected else "[FAIL]"
        print(f"{status} capitalize_words('{text}') = '{result}' (expected '{expected}')")
    
    # Test remove_extra_spaces
    print("\n5. Testing remove_extra_spaces()")
    print("-" * 40)
    
    test_cases_spaces = [
        ("  hello    world  ", "hello world"),
        ("", ""),
        ("   ", ""),
        ("single space", "single space"),
        ("multiple   spaces   here", "multiple spaces here"),
        ("\ttabs\t\tand\tspaces  ", "tabs and spaces")
    ]
    
    for text, expected in test_cases_spaces:
        result = remove_extra_spaces(text)
        status = "[PASS]" if result == expected else "[FAIL]"
        print(f"{status} remove_extra_spaces('{text}') = '{result}' (expected '{expected}')")
    
    # Test error handling
    print("\n6. Testing error handling")
    print("-" * 40)
    
    try:
        count_words(123)
        print("[FAIL] count_words(123) should have raised TypeError")
    except TypeError as e:
        print(f"[PASS] count_words(123) raised TypeError: {e}")
    
    try:
        reverse_text(None)
        print("[FAIL] reverse_text(None) should have raised TypeError")
    except TypeError as e:
        print(f"[PASS] reverse_text(None) raised TypeError: {e}")
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    test_all_functions()
