from spotify_auth import get_spotify_client

sp = get_spotify_client()

user_id = sp.current_user()['id']

playlist = sp.user_playlist_create(
    user=user_id,
    name="Top Arctic Monkey Picks ❄️🐒",
    public=False,
    description="list of songs filtered for no explicit content."
)