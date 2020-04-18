import boto3
import datetime
import pytz
from datetime import datetime, timedelta
#todays_date=datetime.datetime.now()
oldest_date = datetime.now(pytz.utc) - timedelta(days=7)
s3=boto3.client('s3',region_name='ap-south-1')
response=s3.list_objects(Bucket='cf-templates-b8gzjkzq0n1l-ap-south-1')
for i in response['Contents']:
    if(i['LastModified'] < oldest_date):
        print('deleting')
        s3.delete_objects(Bucket='cf-templates-b8gzjkzq0n1l-ap-south-1', 
	Delete={
        'Objects': [
            {
                'Key': i['Key']
                #'VersionId': 'latest'
            },
        ],
        'Quiet': True
    },	
)
        print('deleted')
        print(i['Key'])
#print(i['LastModified'])
#print(response)
