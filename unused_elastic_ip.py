import boto3
ec2_client=boto3.client('ec2',region_name='us-east-1')
address = ec2_client.describe_addresses()
for eip in address['Addresses']:
    if(("InstanceId" not in eip) and ("NetworkInterfaceId" not in eip)):
	print(eip['PublicIp'])
