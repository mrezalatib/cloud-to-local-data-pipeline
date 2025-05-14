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
    connection.row_factory = sqlite3.Row #allows each row to act like a dictionary
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM non_explicit_songs WHERE artist_name = ?""" , (artist,))
    
    results = cursor.fetchall()
    connection.close()

    return results


def get_song_uris():
    songs = get_non_explicit_songs(artist="Arctic Monkeys")
    uris = []

    for song in songs:
        track_name = song['track_name']
        artist_name = song['artist_name']
        query = f"{track_name} {artist_name}"
        
        results = sp.search(q=query, type="track", limit=1) #limit=1 returns only top result
        tracks = results.get('tracks', {}).get('items', [])
        if tracks:
            uris.append(tracks[0]['uri'])
    
    return uris


def add_songs_to_playlist():
    uris = get_song_uris()

    for i in range(0, len(uris), 100):
        sp.playlist_add_items(
            playlist_id=playlist['id'],
            items=uris[i:i+100]
        )
    print("Songs added to playlist")


add_songs_to_playlist()