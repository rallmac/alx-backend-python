#!/usr/bin/env python3
"""This function creates a TestAccessNestedMap class"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """This class inherits from unittest.TestCase"""
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """This method tests the parameterized expand function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

        @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ])
        def test_access_nested_map_exception(self, nested_map, path):
            """This method tests the nested map exception function"""
            with self.assertRaises(KeyError) as context:
                access_nested_map(nested_map, path)
            self.assertEqual(str(context.exception), f"'{path[-1]}'")


if __name__ == '__main__':
    unittest.main()
