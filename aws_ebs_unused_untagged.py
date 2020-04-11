import boto3
ec2=boto3.resource('ec2',region_name='us-east-1')

#emply list which stores all volumes maching criteria
volumes_in_available_state_notagged=[]

#list volumes which are available and not tagged
for vol in ec2.volumes.all():
   #print(vol.id, vol.state)
    if((vol.state=="available") and (vol.tags==None)):
	print(vol.id,vol.state,vol.tags)
	volumes_in_available_state_notagged.append(vol.id)
print(volumes_in_available_state_notagged)
print(len(volumes_in_available_state_notagged))
