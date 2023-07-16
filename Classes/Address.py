import random

class Address:
    def __init__(self):
        self.generateAddress()

    def generateAddress(self):
        street_names = [
        "Maple", "Oak", "Pine", "Cedar", "Elm",
        "First", "Second", "Third", "Fourth", "Fifth",
        "Main", "High", "Park", "Sunset", "River"
        ]
    
        street_types = ["Street", "Avenue", "Road", "Lane", "Court", "Boulevard"]
        
        cities = [
        "Springfield",
        "Harrisonville",
        "Willowbrook",
        "Pleasantville",
        "Greenfield",
        "Fairview",
        "Riverside",
        "Brooksville",
        "Meadowville",
        "Harmony",
        "Sunnydale",
        "Westwood",
        "Oakmont",
        "Crestview",
        "Rockville",
        "Pineville",
        "Cedarhurst",
        "Milton",
        "Glenwood",
        "Havenwood"
        ]
        
        states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California",
        "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
        "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
        "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
        "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
        "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
        "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
        "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
        "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
        "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]
    
        # Generate a random street number between 1 and 9999
        self.street_number = random.randint(1, 9999)
        
        # Select a random street name, type, city, and state
        self.street_name = random.choice(street_names)
        self.street_type = random.choice(street_types)
        self.city = random.choice(cities)
        self.state = random.choice(states)
        
        # Generate a fictional ZIP code
        self.zip_code = str(random.randint(10000, 99999))
    
    

    def outputAddress(self):

        address = f"{self.street_number} {self.street_name} {self.street_type}"
        address += f"\n{self.city}, {self.state} {self.zip_code}"

        return address
