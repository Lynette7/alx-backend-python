# Unittests and Integration Tests

## Tasks To Complete

- test_utils.py: contains a python module that contains a TestAccessNestedMap class that inherits from unittest.TestCase.
- test_utils.py: contains a python module that implements TestAccessNestedMap.test_access_nested_map_exception. It uses the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand):

nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")

- test_utils.py: contains a python module that defines the TestGetJson(unittest.TestCase) class and implements the TestGetJson.test_get_json method to test that utils.get_json returns the expected result. It uses unittest.mock.patch to patch requests.get, and returns a Mock object with a json method that returns test_payload which is parametrized alongside the test_url that will be passed to get_json with the following inputs:
test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}
- test_utils.py: contains a python module that implements the TestMemoize(unittest.TestCase) class with a test_memoize method.
Inside test_memoize, define the following class:
class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()

It uses unittest.mock.patch to mock a_method. Test that when calling a_property twice, the correct result is returned but a_method is only called once using assert_called_once.

- test_client.py: contains a python module that declares the TestGithubOrgClient(unittest.TestCase) class and implements the test_org method. This method tests that GithubOrgClient.org returns the correct value.
It uses @patch as a decorator to make sure get_json is called once with the expected argument but it is not executed.
It uses @parameterized.expand as a decorator to parametrize the test with a couple of org examples to pass to GithubOrgClient, in this order:
google.
abc.
No external HTTP calls are made.
- test_client.py: contains a python module that implements the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url. It uses patch as a context manager to patch GithubOrgClient.org and make it return a known payload.
- test_client.py: contains a python module that implements TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos. It uses @patch as a decorator to mock get_json and make it return a payload of your choice. It uses patch as a context manager to mock GithubOrgClient._public_repos_url and return a value of your choice.
- test_client.py: contains a python module that implements TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.
Parametrize the test with the following inputs:
repo={"license": {"key": "bsd-3-clause"}}, license_key="bsd-3-clause"
repo={"license": {"key": "bsl-1.0"}}, license_key="bsd-3-clause"
- test_client.py: contains a python module that contains the TestIntegrationGithubOrgClient(unittest.TestCase) class and implements the setUpClass and tearDownClass which are part of the unittest.TestCase API. It uses @parameterized_class to decorate the class and parameterize it with fixtures found in fixtures.py.
The setupClass mocks requests.get to return example payloads found in the fixtures. It uses patch to start a patcher named get_patcher, and uses side_effect to make sure the mock of requests.get(url).json() returns the correct fixtures for the various values of url that you anticipate to receive.
- test_client.py: contains a python module that implements the test_public_repos method to test GithubOrgClient.public_repos. The method returns the expected results based on the fixtures. It implements test_public_repos_with_license to test the public_repos with the argument license="apache-2.0" and make sure the result matches the expected value from the fixtures.
