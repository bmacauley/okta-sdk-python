import unittest
from okta import AuthClient


class AuthClientTest(unittest.TestCase):

    def test_client_initializer_args(self):
        client = AuthClient('https://example.okta.com', 'api_key')
        self.assertTrue(client)

    def test_client_initializer_kwargs(self):
        client = AuthClient(base_url='https://example.okta.com',
                            api_token='api_key')
        self.assertTrue(client)

    def test_client_initializer_args_2(self):
        client = AuthClient('https://example.okta.com')
        self.assertTrue(client)

    def test_client_initializer_kwargs_2(self):
        client = AuthClient(base_url='https://example.okta.com')
        self.assertTrue(client)


if __name__ == '__main__':
    unittest.main()
