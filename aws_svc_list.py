# create an inventory of AWS services
# create an empty list
# populate list using append or insert
# print list and length of the list
# Remove two specific services from the list by
#  name or by index
# Print the new list and the new length of the list

# create the initial list of aws services
def initial_list():
    # initialize list empty list
    aws_services = []

    # populate list with a subset of AWS services
    aws_services.append('EC2')
    aws_services.append('Lambda')
    aws_services.append('S3')
    aws_services.append('RDS')
    aws_services.append('Fargate')
    aws_services.append('DynamoDB')
    aws_services.append('RedShift')
    return(aws_services)

# insert a new service
def insert_newservice(exist_list):
    exist_list.insert((len(exist_list)+ 1), 'SageMaker')
    return(exist_list)

# remove 2 services from list
def remove_service(exist_list):
    exist_list.remove('EC2')
    exist_list.remove('S3')
    return(exist_list)

def print_service_list(service_list, list_action):
    if list_action == "initial":
      print('\nThe AWS service initial list includes: \n' + str(service_list))
      print('My initial list of AWS Services includes ' + str(len(service_list)) + ' services.\n')
    elif list_action == "insert":
      print("A new AWS service was inserted in list. List includes: " + str(service_list) + " and includes " + str(len(service_list)) + " services.\n")
    elif list_action == 'remove':
      print("The AWS service list with two items removed includes: " + str(service_list) + " list includes " + str(len(service_list)) + " services.\n")
    else:
      pass
    return()

if __name__ == '__main__':
    # initial service list and print list of services + plus length of the list
    aws_svc_list = initial_list()
    print_service_list(aws_svc_list, "initial")

    # insert new service and print new list + plus the length list
    aws_svc_list = insert_newservice(aws_svc_list)
    print_service_list(aws_svc_list, "insert")

    # remove a service from list and then print list with item removed + length of list
    aws_svc_list = remove_service(aws_svc_list)
    print_service_list(aws_svc_list, "remove")
