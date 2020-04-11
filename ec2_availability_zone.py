# script that lists machines which are launched in other
import boto3
ec2_client= boto3.client('ec2',region_name='us-east-1')
response = ec2_client.describe_instances(
	Filters = [{
	'Name': 'availability-zone',
	'Values': ['us-east-1a','us-east-1b','us-east-1d','us-east-1e']
	}])
#print(response)
instance_ids_az=[]
for inst in response['Reservations']:
    for inst_id in inst['Instances']:
	instance_ids_az.append(inst_id['InstanceId'])

print(instance_ids_az)
print(len(instance_ids_az))
