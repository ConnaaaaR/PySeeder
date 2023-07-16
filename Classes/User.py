import hashlib
from Classes.Person import Person

class User(Person):
    def __init__(self):
        super().__init__()
        self.email = self.generateEmail()
        self.password = self.generatePassword()
        
    def generateEmail(self):
        domain = '@email.com'
        email = self.fname + self.lname + domain
        return email.lower()
    
    def generatePassword(self):
        value = 'password'
        hash_object = hashlib.sha256()
        hash_object.update(value.encode('utf-8'))

        hashed_value = hash_object.hexdigest()
        return hashed_value

        