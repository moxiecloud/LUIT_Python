# Allow the user to enter the number of EC2 instances that require names
#   Convert to integer ex. int(input())
# Allow user to enter their Department name
#   Check that the first letter is capitalized
#   Check that all text entered are strings
# Generate random characters and numbers that will be included in the EC2 instance
# name to assure that the EC2 instance name is unique
#   Put the department name at the beginning of the name to easily identify the Department
# Print the names that will be used for the EC2
#

import random
import string

# Valid department list
dept_list = ['Accounting', 'Marketing', 'FinOps']

# EC2 instance list
EC2_Instances = []

print('\nEC2 instance unique name generator.\n')

num_instance_names = int(input('Enter the number of EC2 instance names you need: '))

# User enters department name, the first letter of dept is capitalized & will be
# concatenated with the generated random characters and numbers to assure instance
# name unique
dept_name = input('Enter Department Name: ')
dept_name = dept_name.title()

# Generate unique names for EC2 instances based on number of names needed
for _ in range(num_instance_names):

    N = 8
    res = ''.join(random.choices(string.ascii_uppercase +  string.digits, k = N))

    EC2_Instances.append((dept_name + '-' + str(res)))

print("\nList of unique names for your department EC2 instances:")
print('\n'.join(EC2_Instances))
