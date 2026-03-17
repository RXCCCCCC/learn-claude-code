"""Tests for the utils module."""

import unittest
from utils import add, greet, sum_list


class TestAdd(unittest.TestCase):
    """Test cases for the add function."""

    def test_positive_numbers(self) -> None:
        """Test adding positive numbers."""
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self) -> None:
        """Test adding negative numbers."""
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self) -> None:
        """Test adding with zero."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""

    def test_simple_name(self) -> None:
        """Test greeting with a simple name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_empty_string(self) -> None:
        """Test greeting with an empty string."""
        self.assertEqual(greet(""), "Hello, !")

    def test_special_characters(self) -> None:
        """Test greeting with special characters."""
        self.assertEqual(greet("John-Doe"), "Hello, John-Doe!")


class TestSumList(unittest.TestCase):
    """Test cases for the sum_list function."""

    def test_positive_numbers(self) -> None:
        """Test summing positive numbers."""
        self.assertEqual(sum_list([1, 2, 3, 4]), 10)

    def test_negative_numbers(self) -> None:
        """Test summing negative numbers."""
        self.assertEqual(sum_list([-1, -2, -3]), -6)

    def test_mixed_numbers(self) -> None:
        """Test summing mixed positive and negative numbers."""
        self.assertEqual(sum_list([5, -3, 2, -1]), 3)

    def test_empty_list(self) -> None:
        """Test summing an empty list."""
        self.assertEqual(sum_list([]), 0)


if __name__ == "__main__":
    unittest.main()
