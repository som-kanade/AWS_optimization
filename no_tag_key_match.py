import boto3
client=boto3.client('ec2',region_name='us-east-1')
response=client.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
	if "Business" not in [tag['Key'] for tag in instance['Tags']]:
	    print(instance['InstanceId'])
