from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

client = BackendApplicationClient(client_id='your_client_id')
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://eu.battle.net/oauth/token', client_id='your_client_id',
        client_secret='your_client_secret')
access_token = token['access_token']


def get_token():
    return access_token
