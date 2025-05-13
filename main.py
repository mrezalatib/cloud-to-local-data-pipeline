import boto3
import pandas as pd
from io import StringIO


#creates s3 client object (facilitates communication between AWS S3 and python) 
s3 = boto3.client("s3")

bucket_name = "my-spotify-stats-bucket"
file_name = "spotifydataset.csv"

response = s3.get_object(Bucket=bucket_name, Key=file_name) #sends request to AWS to retrieve specified csv data

csv_content = response['Body'].read().decode('utf-8') #decode utf-8 makes response body human readable
df = pd.read_csv(StringIO(csv_content)) #csv_content passed through String_IO because pd.read_csv expects a file or file-like object (not a string)

#preview data from response body on console
print(df.head())
