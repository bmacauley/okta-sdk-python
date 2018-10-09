import vcr
from okta import AuthClient

OKTA_URL = 'https://dev-513447-admin.oktapreview.com'
API_TOKEN = '00po9bVL_pj6SzDx4AS0aQbWRWE_8BxQkm2SI_V_LK'
# no MFA, API token
OKTA_USER1 = 'okta-test-user1@mailinator.com'
OKTA_USER1_PWD = 'Totalmanner1'
# MFA
OKTA_USER2 = 'okta-test-user2@mailinator.com'
OKTA_USER2_PWD = 'Onlyocean1'

my_vcr = vcr.VCR(serializer='yaml',
                 cassette_library_dir='tests/fixtures\
                                    /vcr_cassettes/test_authclient',
                 record_mode='new_episodes',)


class TestInstantiation:

    # AuthClient initialization - no API token/trusted application
    def test_client_initializer_kwargs_2(self):
        client = AuthClient(base_url=OKTA_URL)
        assert(client)

    def test_authclient_initialization_args_2(self):
        client = AuthClient(OKTA_URL)
        assert(client)

    # AuthClient initialization - API key
    def test_client_initializer_kwargs_1(self):
        client = AuthClient(base_url=OKTA_URL,
                            api_token=API_TOKEN)
        assert(client)

    def test_authclient_initialization_args_1(self):
        client = AuthClient(OKTA_URL, API_TOKEN)
        assert(client)


# authenticate

class TestAuthenticate:

    @my_vcr.use_cassette('test_authenticate.yaml')
    def test_authenticate(self):
        client = AuthClient(base_url=OKTA_URL)
        auth = client.authenticate(OKTA_USER1,
                                   OKTA_USER1_PWD)
        assert(auth.status == 'SUCCESS')

    @my_vcr.use_cassette('test_authenticate_fail.yaml')
    def test_authenticate_fail(self):
        client = AuthClient(base_url=OKTA_URL)
        try:
            client.authenticate(OKTA_USER1, 'xxxx')
        except Exception as e:
            assert 'Authentication failed' in str(e)

    @my_vcr.use_cassette('test_authenticate_mfa.yaml')
    def test_authenticate_mfa(self):
        client = AuthClient(base_url=OKTA_URL)
        auth1 = client.authenticate(OKTA_USER2,
                                    OKTA_USER2_PWD)
        # assert(auth1.status == 'MFA_REQUIRED')
        mfa_token = '470877'
        auth2 = client.auth_with_factor(auth1.stateToken,
                                        auth1.embedded.factors[0].id,
                                        mfa_token)
        assert(auth1.status == 'MFA_REQUIRED' and auth2.status == 'SUCCESS')

    # @my_vcr.use_cassette('test_authenticate_trusted_app.yaml')
    # def test_authenticate_trusted_app(self):
    #     client = AuthClient(base_url=OKTA_URL,
    #                         api_token=API_TOKEN)
    #     auth = client.authenticate(OKTA_USER1,
    #                                OKTA_USER1_PWD)
    #     assert(auth.status == 'SUCCESS')
