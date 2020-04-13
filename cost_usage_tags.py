import boto3
ce_client=boto3.client('ce',region_name='us-east-1')

response=ce_client.get_cost_and_usage(
TimePeriod={
        'Start': '2020-04-01',
        'End': '2020-04-12'
    },
Filter = {
'Tags':{'Key':'Business','Values':['teama','teamb']}},
Granularity='MONTHLY',
Metrics=[
        'AmortizedCost',
	'BlendedCost',
	'UnblendedCost'
    ]
)
#print(response)
for cost in response['ResultsByTime']:
    #print(cost['Total']['UnblendedCost'])
    print('Unblended cost is',cost['Total']['UnblendedCost']['Amount'])
    #print(cost['Total']['BlendedCost']['Amount'])
    #print(cost['Total']['AmortizedCost']['Amount'])
