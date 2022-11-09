import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Get environment variables
load_dotenv()
SPOTIFY_ID = os.getenv('spotify_client_id')
SPOTIFY_SECRET = os.getenv('spotify_cient_secret')
# print(f"{SPOTIFY_ID}, {SPOTIFY_SECRET}")

# authenticating to spotify using Spotify and getting the results
# from spotipy.oauth2 import SpotifyClientCredentials
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
date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=URL)
response.raise_for_status()
website = response.text

soup = BeautifulSoup(website, "html.parser")
# print(soup.prettify())
songs_list = soup.select(selector=".o-chart-results-list-row-container li h3")
songs = [song.getText().replace("\n", "").replace("\t\t\t\t\t\t\t\t\t", "").replace("\t\t\t", "") for song in
         songs_list]
print(songs)

# ----- Code to get the song number -------------------- #
# num_list = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-background-color-black lrv-u-color-white u-width-100 u-width-55@mobile-max u-width-55@tablet-only lrv-u-height-100p lrv-u-flex lrv-u-flex-direction-column@mobile-max lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey")
# ranks = [num.text.split()[0] for num in num_list]
# # print(ranks)

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
