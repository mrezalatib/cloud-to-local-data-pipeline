import boto3
import pandas as pd
from io import StringIO


def load_csv_from_s3(bucket_name: str, file_name: str) -> pd.DataFrame:
    #creates s3 client object
    s3 = boto3.client("s3")

    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    csv_data = response['Body'].read().decode('utf-8') #decode utf-8 makes response body human readable

    #csv_content passed through String_IO because pd.read_csv expects a file or file-like object (not a string)
    df = pd.read_csv(StringIO(csv_data))

    return df


bucket_name = "my-spotify-stats-bucket"
file_name = "spotifydataset.csv"

df = load_csv_from_s3(bucket_name, file_name)
 
print(df.head()) #a preview of data from response body (its not ALL the data since its too large to display via terminal ofc)