import pymysql
import time
import sys
from os import system as os
from Classes.Person import Person
from Classes.User import User

###############################
# Change these variables to your db credentials
# no other changes to this file are required.
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DATABASE = 'wcDB'
###############################

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
        person = User()
        print(vars(person))
        cursor = cnx.cursor()
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

def exporter():
    # this will export an array to json or csv.

def generator():
    # generate data arrays for use with export
