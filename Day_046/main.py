from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
music_date_input = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{music_date_input}")
soup = BeautifulSoup(response.text, "html.parser")
all_title = soup.find_all(
    name="h3", class_="a-no-trucate")
titles = []
for title in all_title:
    temp_title = title.getText()
    temp_title = temp_title.strip('\n' '\t')
    titles.append(temp_title)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri=os.environ.get(
        "redirect_uri"),
    client_id=os.environ.get("client_id"),
    client_secret=os.environ.get(
        "client_secret"),
    show_dialog=True,
    cache_path="token.txt"))


user_id = sp.current_user()["id"]
song_uris = []
year = music_date_input[0:4]
for music in titles:
    result = sp.search(
        q=f"track:{music} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{music} doesn't exist in spotify")


playlist = sp.user_playlist_create(
    user=user_id, name=f"{year} Billboard 100", public=False, description="")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
