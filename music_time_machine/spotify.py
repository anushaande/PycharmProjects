import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Get environment variables
load_dotenv()
SPOTIFY_ID = os.getenv('spotify_client_id')
SPOTIFY_SECRET = os.getenv('spotify_cient_secret')
# print(f"{SPOTIFY_ID}, {SPOTIFY_SECRET}")

# authenticating to spotify using Spotify and getting the results
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_ID,
#                                                            client_secret=SPOTIFY_SECRET))

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        redirect_uri="https://example.com/callback",
        scope="playlist-modify-private",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    ))

user_id = sp.current_user()["id"]

print(user_id)
