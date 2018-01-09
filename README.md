# boto3
Code for searching AWS instances with search criteria using boto3
This script uses Boto3.Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.
It asks for input from user regarding the region that they want to enter(according to the exercise question). 
Using boto3 library, ec2 instances of the region are retrieved and stored in ec2 variable.
The script then asks for input from user regarding the value of the tag of the resources they want to retrive.
If the user needs resources which start from 'Centos', Centos* can be given as an input for the same.
Filters is used to put in the field and the value on the basis of which resources will be retrieved.
These filter values are assigned to instances variable as list.
The next statement (Line 27,28) print the number of instances with the required tag.
The next statement (Line 31,32) prints the instances with the Name/ID with the inputted tag.
