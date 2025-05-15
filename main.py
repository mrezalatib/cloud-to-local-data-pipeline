from data_loader import load_csv_from_s3, write_to_sqlite, filter_non_explicit_songs
from playlist_creator import add_songs_to_playlist


def main():

    bucket_name = "my-spotify-stats-bucket"
    file_name = "spotifydataset.csv"

    df = load_csv_from_s3(bucket_name, file_name)
    write_to_sqlite(df, 'spotify_stats.db', 'spotify_statistics')
    filter_non_explicit_songs()

    add_songs_to_playlist()

if __name__ == "__main__":
    main()