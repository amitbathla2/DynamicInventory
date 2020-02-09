import boto3
ec2 = boto3.resource('ec2')
ec2.create_tags(Resources=['i-0a25c948edc2894fc'], Tags=[{'Key':'name', 'Value':'apphostname'}])
