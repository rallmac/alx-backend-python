#!/usr/bin/env python3
"""Unit tests for GithubOrgClient and utils functions"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method of GithubOrgClient"""
        # Arrange: define mock data for get_json and _public_repos_url
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_payload

        # Patch _public_repos_url directly as a property
        repo_url_patch = patch.object(
            GithubOrgClient,
            '_public_repos_url',
            return_value="https://api.github.com/orgs/test-org/repos"
        )
        with repo_url_patch:
            # Act: initialize client and call public_repos
            client = GithubOrgClient("test-org")
            repos = client.public_repos()

            # Assert: verify repos list matches expected names
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos"
            )

    @patch('client.GithubOrgClient.org', new_callable=Mock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property of GithubOrgClient"""
        # Arrange: set up the mock to return a dictionary when accessed
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"
        }

        # Act: initialize client and retrieve _public_repos_url
        client = GithubOrgClient("test-org")
        result = client._public_repos_url

        # Assert: verify _public_repos_url is as expected
        self.assertEqual(result, "https://api.github.com/orgs/test-org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method of GithubOrgClient"""
        # Act: create client and check has_license
        client = GithubOrgClient("test-org")
        result = client.has_license(repo, license_key)

        # Assert: verify the result matches the expected value
        self.assertEqual(result, expected)


org_payload = {"key": "value"}
repos_payload = [{"name": "repo1"}, {"name": "repo2"}]
expected_repos = ["repo1", "repo2"]
apache2_repos = ["repo1"]


@parameterized_class(
    [
        {"org_payload": org_payload,
         "repos_payload": repos_payload,
         "expected_repos": expected_repos,
         "apache2_repos": apache2_repos},
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up the test case"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side_effects based on anticipated URLs
        def json_side_effect(url):
            return cls.get_mock_payload(url)

        cls.mock_get.side_effect = lambda url: Mock(json=json_side_effect)

    @classmethod
    def tearDownClass(cls):
        """Tear down the test case"""
        cls.get_patcher.stop()

    @classmethod
    def get_mock_payload(cls, url):
        """Return the appropriate mock payload based on the URL"""
        if url == "https://api.github.com/orgs/test-org":
            return cls.org_payload
        elif url == "https://api.github.com/orgs/test-org/repos":
            return cls.repos_payload
        return {}

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("test-org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_apache2_repos(self):
        """Test retrieval of Apache2 repositories"""
        client = GithubOrgClient("test-org")
        repos = client.public_repos()
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
