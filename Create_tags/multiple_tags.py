
import boto3
ec2 = boto3.resource('ec2')
l=["name:amit", "name1:bathla"]
for key in l:
   tag=key.split(":")[0]
   print(tag)
   value=key.split(":")[1]
   print(value)
   ec2.create_tags(Resources=['i-0a25c948edc2894fc'], Tags=[{'Key':tag, 'Value':value}])
