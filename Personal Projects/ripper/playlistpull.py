import spotipy
import os
from settings import client_id, client_secret
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

results = sp.search(q='black rebel motorcyle club', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])