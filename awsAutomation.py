import boto3

ec2 = boto3.client('ec2')

try:
    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc['Vpc']['VpcId']
    print('vpc created successfully - ' + vpc_id)

    subnet = ec2.create_subnet(CidrBlock='10.0.0.0/24', VpcId=vpc_id)
    subnet_id = subnet['Subnet']['SubnetId']
    print('subnet created successfully - ' + subnet_id)
except:
    print('Something went wrong while creating vpc with subnet')
    exit()

key_pair_name = ''
key_names = ['aanchal_key_pair_new']
try:
    response = ec2.describe_key_pairs(KeyNames=key_names)
    key_pair_name = response['KeyPairs'][0]['KeyName']
except:
    key_pair = ec2.create_key_pair(KeyName=key_names[0])
    with open('C:\\Users\\aanchalgupta\\PycharmProjects\\pythonProject\\venv\\key\\my_key.pem', 'w') as file:
        file.write(key_pair['KeyMaterial'])
    key_pair_id = key_pair['KeyPairId']
    key_pair_name = key_pair['KeyName']

print(key_pair_name)

instance = ec2.run_instances(ImageId='ami-0557a15b87f6559cf', InstanceType='t2.micro', KeyName=key_pair_name, MaxCount=2, MinCount=1, NetworkInterfaces=[{'AssociatePublicIpAddress': True, 'DeviceIndex':0, 'SubnetId': subnet_id}])
instance_id = instance['Instances'][0]['InstanceId']
print('ec2 instance [' + instance_id + '] created successfully')

try:
    instance = ec2.run_instances(ImageId='ami-0557a15b87f6559cf', InstanceType='t2.micro', KeyName=key_pair_name, SubnetId=subnet_id, MaxCount=2, MinCount=1, NetworkInterfaces=[{'AssociatePublicIpAddress': True}])
    instance_id = instance['Instances'][0]['InstanceId']
    print('ec2 instance [' + instance_id + '] created successfully')
except:
    ec2.delete_subnet(SubnetId=subnet_id)
    ec2.delete_vpc(VpcId=vpc_id)
    print('Could not create an EC2 instance')
    exit()

try:
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket='aanchal-bucket')
    s3.upload_file('venv\index.html', 'aanchal-bucket', 'index.html')
    print('html file uploaded successfully')
except:
    print('Something went wrong while creating or updating the S3 bucket')
    exit()

s3.put_bucket_website(Bucket='aanchal-bucket', WebsiteConfiguration={'IndexDocument': {'Suffix': 'index.html'}})