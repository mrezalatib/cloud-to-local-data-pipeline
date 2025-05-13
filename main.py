import boto3
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def load_csv_from_s3(bucket_name: str, file_name: str) -> pd.DataFrame:
    #creates s3 client object
    s3 = boto3.client("s3")

    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    csv_data = response['Body'].read().decode('utf-8') #decode utf-8 makes response body human readable

    #csv_content passed through String_IO because pd.read_csv expects a file or file-like object (not a string)
    df = pd.read_csv(StringIO(csv_data))

    return df


def write_to_sqlite(df, database_name: str, table_name: str):
    try:
        engine = create_engine(f'sqlite:///{database_name}') #create engine which is connection to specified db. sets configs for connection
        df.to_sql(table_name, con=engine, index=False, if_exists='replace') #create + write datafram to db. index = false because pandas adds index column i dont need that
        print(f"Data written to '{table_name}' table in '{database_name}' successfully.")
    except SQLAlchemyError as e:        
        print(f"Error: {e}")

bucket_name = "my-spotify-stats-bucket"
file_name = "spotifydataset.csv"

df = load_csv_from_s3(bucket_name, file_name)
write_to_sqlite(df, 'spotify_stats.db', 'spotify_statistics')
