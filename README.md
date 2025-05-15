# Non-Explicit Spotify Playlist Generator

Automatically generate custom Spotify playlists filtered for **non-explicit songs** by your specified artists.

## What It Does

- Downloads Spotify data from S3 bucket
- Filters it for **non-explicit** tracks by a specified artist
- Uses the Spotify API to create a curated playlist
- Adds those clean tracks to your Spotify account

## Tech Stack

- Python
- SQLite for local storage
- Spotipy for interacting with Spotify API
- Boto3 for AWS S3 data handling

## How to Use

1. clone the repo: 
2. create an S3 bucket called "my-spotify-stats-bucket"
3. add your spotify data in csv format to s3
4. configure aws environment (access key + secret access key)
5. create spotify app on spotify for devs
6. set login credentials for spotify app as environment variables (client id, client secret, your callback uri)

## Note

Spotify data in s3 bucket is dummy data for now.
