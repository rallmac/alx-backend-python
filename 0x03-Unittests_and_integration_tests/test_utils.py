#!/usr/bin/env python3
"""This function creates a TestAccessNestedMap class"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """This class implements TestGetJson class and inherits
       from unitest.TestCase
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected result with
           a mocked request.get
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch("utils.requests.get") as mock_get:
            mock_get.return_value = mock_response
            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """This class implements TestMemoize and inherits from
       unittsts.TestCase
    """

    def test_memoize(self):
        """Test that memoize caches the result of a_property"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        test_instance = TestClass()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
