from spotify_auth import get_spotify_client
import sqlite3

sp = get_spotify_client()

user_id = sp.current_user()['id']

playlist = sp.user_playlist_create(
    user=user_id,
    name="Top Arctic Monkey Picks ❄️🐒",
    public=False,
    description="list of songs filtered for no explicit content."
)


def get_non_explicit_songs(artist: str):
    connection = sqlite3.connect('spotify_stats.db')
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM non_explicit_songs WHERE artist_name = ?""" , (artist,))
    
    results = cursor.fetchall()
    connection.close()

    return results


def add_songs_to_playlist():
    pass

