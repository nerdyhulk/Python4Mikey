import base64
from http import client
from importlib import import_module
from secrets import token_urlsafe
import requests
import os
import local_settings
import spotipy
import base64
import datetime

SCOPE = 'https://api.spotify.com/'

client_id = local_settings.client_id
client_secret = local_settings.client_secret

class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'
    
    def __init__(self, client_id, client_secret):
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        
    def get_client_creds_b64(self):
        '''
        Return a base64 encoded string
        '''
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None;
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{local_settings.client_id}:{local_settings.client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
    
    def get_token_header(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            'Authorization': f'Basic {client_creds_b64}'
        }
    def get_token_data(self):
        return {
            'grant_type': 'client_credentials',
        }
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            data = r.json()
            now = datetime.datetime.now()
            access_token = data['access_token']
            expires_in = data['expires'] #seconds
            expires = now + datetime.timedelta(seconds=expires_in)
            self.access_token_expires = expires
            self.access_token_did_expire = expires < now
            return True
    

print(client_id)





