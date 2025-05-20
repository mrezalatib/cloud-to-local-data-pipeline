from spotify_auth import get_spotify_client
import sqlite3

sp = get_spotify_client()


def get_non_explicit_songs(artist: str):
    """
    Retrieves non-explicit songs from the non_explicit_songs table in SQLite db based on specified artist

    Args:
        artist (str): the name of the artist whose non-explicit songs to be retrieved from the db.

    Returns: 
        list[sqlite3.Row]: a list of song data where each list item behaves like a dict.
    """
    connection = sqlite3.connect('spotify_stats.db')
    connection.row_factory = sqlite3.Row #allows each row to act like a dictionary
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM non_explicit_songs WHERE artist_name = ?""" , (artist,))
    
    results = cursor.fetchall()
    connection.close()

    return results


def get_song_uris():
    """
    Searches spotify using spotify api for songs from the db, collects song uniform resource identifier,
    adds uri to list.

    Returns:
        list[str]: a list of uris of songs found via search on spotify.
    """
    artist = input("Please select an artist: ")
    songs = get_non_explicit_songs(artist= artist)
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
    """
    Takes list of spotify songs uris and adds each item to the playlist.
    """
    uris = get_song_uris()
    user_id = sp.current_user()['id']

    name_of_playlist = input("Please enter a name for the playlist: ")
    playlist = sp.user_playlist_create(
        user=user_id,
        name=name_of_playlist,
        public=False,
        description="list of songs filtered for no explicit content."
    )

    for i in range(0, len(uris), 100):
        sp.playlist_add_items(
            playlist_id=playlist['id'],
            items=uris[i:i+100]
        )
    print("Songs added to playlist")
