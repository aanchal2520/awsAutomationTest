# awsAutomationTest

The project uses AWS' SDK for Python (Boto3) to access services on AWS and perform the below mentioned tasks.
-> First we create a VPC using the create_vpc() API call
-> We then create a subnet in the created VPC using the create_subnet() API call
-> We create a key pair for our EC2 instance. We check if the key pair exists using the describe_key_pair() API call, in which case we use the existing key pair at the time of instance creation. In the case the key pair does not exist, we create a new key pair using the create_key_pair() API call.
-> We then create an EC2 instance attached to the subnet and specify the key pair created in the previous step using the run_instance() API call.
-> On successful creation of the EC2 instance, we create an S3 bucket using the create_bucket() API and upload our html file to this bucket with the help of upload_file() API.
-> Lastly we configure the bucket as a static website using the put_bucket_website() API 

KEY Terminologies:
VPC: VPC stands for virtial private cloud which is a range of IP Addresses in the cloud where one's AWS resources are hosted and accessible
Subnet: Subnet is another sub segregation of IP ranges inside the VPC
EC2: Amazon EC2 is a web service that provides resizable compute capacity in the cloud. It is essentially a Virtual Machine hosted on the cloud with scalable compute capacity. 
S3: It is a scalable cloud storage service
