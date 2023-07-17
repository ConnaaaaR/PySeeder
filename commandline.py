import pymysql
import time
import sys
import json
import csv
from os import system as os
from Classes.Person import Person
from Classes.Address import Address
from Classes.User import User

###############################
# Change these variables to your db credentials
# no other changes to this file are required.
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DATABASE = 'database_name'
###############################


def generator():
    class_input = input('what should be created? ')
    class_type = globals().get(class_input.capitalize())
    num_instances = int(input('Enter number of instances to create '))
    instances = []
    for _ in range(num_instances):
        instance = class_type()
        instances.append(instance)
    return {'class_name': class_input, 'instances': instances}


def exporter():
    file_format = input('what format? (csv / json) ')

    data = generator()
    
    filename = f"{data['class_name']}.{file_format}"
    instances = data['instances']
    try:
        if file_format == "csv":
            with open(filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(instances[0].__dict__.keys())

                for instance in instances:
                    writer.writerow(instance.__dict__.values())
                
        elif file_format == "json":
            with open(filename, "w") as jsonfile:
                json.dump(data, jsonfile, indent=4)

        else:
            print("Invalid file format. Supported formats: csv, json")
    except Exception as e:
        print(str(e))
    sys.exit('done!')



database_connection = input ('Do you want to connect directly to a local database? (y/n): ')

if (database_connection.lower() == 'y'):
    attempts = 0
    maxAttempts = 5
    waitTime = 3
    while (attempts <= maxAttempts ):
        ts = time.strftime("%H:%M:%S", time.localtime())
        try:
            cnx = pymysql.connect(
                user=USERNAME,
                password=PASSWORD,
                host=HOST,
                database=DATABASE
            )
            cursor = cnx.cursor()
            address_instances = generator()
            break
        
        except Exception as e:
            if (attempts < maxAttempts-1):
                print('[{}] Connection to database failed ({}/{}). Trying again in {} seconds...  (Error: {})'.format(ts,attempts+1,maxAttempts,round(waitTime),str(e)))
                time.sleep(waitTime)
                attempts += 1
                waitTime = waitTime * 1.5
            else: 
                sys.exit('[{}] Connection to database failed after {} attempts. Exiting program.'.format(ts,maxAttempts))
                break
    cnx.commit()
    cnx.close()
else:
    # generator()
    exporter()
