# list snapshots which are older than 30 days
import boto3
import pytz
from datetime import datetime, timedelta

ec2_client=boto3.client('ec2',region_name='us-east-1')
snapshots=ec2_client.describe_snapshots(OwnerIds=['self'])['Snapshots']
oldest_date = datetime.now(pytz.utc) - timedelta(days=1)
for snaps in snapshots:
    if(snaps['StartTime'] < oldest_date):
         print(snaps['SnapshotId'], 'has volume of', snaps['VolumeSize'])
        #print(snaps['SnapshotId'])
