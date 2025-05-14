from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_client():
    """
    Loads env variables for auth process (client secret, client id, callback uri)

    Returns spotify client: this is to prevent having to repeatedly start new clients. this one will be imported where necessary
    """
    load_dotenv()
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public playlist-modify-private"))
