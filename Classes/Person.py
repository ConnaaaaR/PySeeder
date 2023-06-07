import json
import random

file = open('Data/names.json')
data = json.load(file)

class Person:
    def __init__(self):
        self.sex = self.setSex()
        self.setName()
        self.age = random.randint(18,55)
        

    def getName(self):
        name = self.fname + ' ' + self.lname
        return name

    def getAll(self):
        selfArr = [self.fname,
                   self.lname,
                   self.age,
                   self.sex
                ]
        return selfArr

    def setSex(self):
        sex = ['Male', 'Female']
        result = sex[random.randint(0,1)]
        return result

    def setName(self):
        if(self.sex == 'Male'):
            self.fname = random.choice(data['male_first_names'])
            self.lname = random.choice(data['last_names'])
        else:
            self.fname = random.choice(data['female_first_names'])
            self.lname = random.choice(data['last_names'])
