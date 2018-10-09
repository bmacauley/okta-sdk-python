from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.auth.AuthResult import AuthResult


class OidcClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/oauth2/v1'
        ApiClient.__init__(self, *args, **kwargs)

    def authorize(self, idp, session_token, response_type, client_id,
                  redirect_uri, display, max_age, response_mode, scope,
                  state, prompt, nonce, code_challenge, code_challenge_method,
                  login_hint, idp_scope):

        # headers = {}
#        request = {}
        params = {}
        url_path = '/oauth2/v1/authorize'
        response = ApiClient.get_path(self, url_path,
                                      request=None, params=params)
        pass

    def token(self, grant_type, code, refresh_token, username, password, scope,
              redirect_uri, code_verfier, client_id, client_secret,
              client_assertion, client_assertion_type):
        headers = {}
        request = {}
        params = {}
        url_path = {}
        pass

    def introspect(self, token, token_type_hint, client_id, client_secret,
                   client_assertion, client_assertion_type):
        headers = {}
        request = {}
        params = {}
        url_path = '/oauth2/v1/introspect'
        response = ApiClient.get_path(self, url_path, headers,
                                      request, params=params)
        pass

    def revoke(self, token, token_type_hint, client_id, client_secret,
               client_assertion, client_assertion_type):
        headers = {}
        request = {}
        params = {}
        url_path = {}
        pass

    def keys(self, client_id=None):
        headers = {}
        request = {}
        params = {}
        url_path = {}
        pass

    def userinfo(self, access_token):
        headers = {
            'Content-Type': 'Authorization: Bearer {0}'.format(access_token)
        }
        #request = {}
        #params = {}
        url_path = '/oauth2/v1/userinfo'
        response = ApiClient.get_path(self, url_path, headers,
                                      request, params=params)
        return Utils.deserialize(response.text, AuthResult)

    def logout(self, id_token_hint, post_logout_redirect_uri, state):
        headers = {}
        request = {}
        params = {}
        url_path = {}
        pass

    def oidc_discovery(self):
        #headers = {}
        #request = {}
        #params = {}
        url_path = '/.well-known/openid-configuration'

        response = ApiClient.get_path(self, url_path,
                                      request=None, params=None)
        self.discovery = Utils.deserialize(response.text, AuthResult)
        return Utils.deserialize(response.text, AuthResult)
