import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
scope = ["user-read-recently-played",
"user-read-private",
"user-read-email",
"streaming",
"user-modify-playback-state",
"user-read-playback-state",
"user-read-recently-played"]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

devices = sp.devices()
sp.volume(10, devices["devices"][0]["id"])
# PREMIUM_REQUIRED