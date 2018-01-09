#!/usr/bin/env python3 
# Author: Nandika Shendre

# Importing boto3 library
import boto3 

# Taking input for region name from user
region = input("Enter the region: ")

# Use default value 'us-west-2'
# If region not entered by user

# Using boto library
# Retrieving ec2 instances with the region input 
ec2 = boto3.resource('ec2', region_name=region) 

# Taking input for values
input_value = input("Enter value of instances (insert * at the end, if you want to display all results starting with given input): ")

# Using filters for name and value
filters = [{'Name':'tag:Name', 'Values':[input_value]}] 

# Assigning filter values to the instance
instances = list(ec2.instances.filter(Filters=filters)) 

# Printing count of the resources starting with the given input
print("Count of Sort: ") 
print(len(instances)) 

# Printing name/ID of the resources starting with the given input
print("Name/ID: ") 
print(instances)
