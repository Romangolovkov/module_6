import unittest
from unittest import mock
import requests


def unique_numbers(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


class TestUniqueNumbers(unittest.TestCase):
    def test_unique_numbers1(self):
        result = unique_numbers([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(result, second = [1, 2, 3, 4, 5, 6, 7])

    def test_unique_numbers2(self):
        result = unique_numbers([1, 1, 3, 3, 5, 7, 7])
        self.assertEqual(result, second = [1, 3, 5, 7])

    def test_unique_numbers3(self):
        result = unique_numbers([1, 1, 3, 3, 5, 7, 7])
        self.assertEqual(result, second = [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()