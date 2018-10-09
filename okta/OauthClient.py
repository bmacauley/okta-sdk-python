from okta.framework.ApiClient import ApiClient
from okta.framework.ApiClient import HttpClient
from okta.framework.Utils import Utils
from okta.models.auth.AuthResult import AuthResult


class OauthClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/oauth2/'
        ApiClient.__init__(self, *args, **kwargs)


    def authorize():
        pass

    def token():
        pass

    def introspect():
        pass

    def revoke():
        pass

    def logout():
        pass

    def keys():
        pass

    def oauth_server_metadata():
        pass

    def oidc_server_metadata():
        pass



class OauthServerClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/oauth2/'
        ApiClient.__init__(self, *args, **kwargs)

