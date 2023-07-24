# commandline.py
import pymysql
import time
import sys
import json
import csv
from tqdm import tqdm 
from os import system as os
from Classes.Person import Person
from Classes.Address import Address
from Classes.Company import Company 
from Classes.User import User

###############################
# Change these variables to your db credentials
# no other changes to this file are required.
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DATABASE = 'database_name'
###############################

def generator(class_input=None, num_instances=None):
    if class_input is None:
        class_input = input('what should be created? ')
    if num_instances is None:
        num_instances = int(input('Enter number of instances to create '))

    # Use tqdm for progress bar when creating over 10000 instances
    if num_instances > 10000:
        print("Creating instances...")
        instances = []
        for i in tqdm(range(num_instances), unit="instance"):
            class_type = globals().get(class_input.capitalize())
            instance = class_type()
            instances.append(instance)
    else:
        class_type = globals().get(class_input.capitalize())
        instances = [class_type() for _ in range(num_instances)]

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
        return 'done!'
    except Exception as e:
        print(str(e))
        return 'error'
    

def connect_to_database():
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
        exporter()

if __name__ == '__main__':
    connect_to_database()
