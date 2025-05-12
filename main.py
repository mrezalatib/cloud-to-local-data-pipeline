import boto3
import pandas as pd
from io import StringIO



s3 = boto3.client("s3")

bucket_name = "my-spotify-stats-bucket"
file_name = "spotifydataset.csv"

response = s3.get_object(Bucket=bucket_name, Key=file_name)

csv_content = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_content))

# Preview the data
print(df.head())
