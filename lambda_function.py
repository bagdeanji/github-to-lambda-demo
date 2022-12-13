import boto3
import json

region = 'ap-south-1'
instances = ['i-0a46ab2f0eb547e22']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
    print('sucess')
