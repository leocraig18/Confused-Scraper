import random 
from datetime import datetime

class Car:
    def __init__(self, manufacturer=None, model=None, reg_number=None):
        self.manufacturer = manufacturer
        self.model = model
        self.reg_number = reg_number

    def __str__(self):
        print(f"{self.manufacturer} {self.model} Info\n")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Model: {self.model}")
        print(f"Registration Number: {self.reg_number}\n")

class Person:
    def __init__(self, name, dob, car, postcode, time_licence_held=None):         
        self.title = name[0]
        self.first_name = name[1]
        self.last_name = name[2]
        self.race = name[3]
        self.dob = dob
        self.postcode = postcode
        self.phone_number = self.generate_fake_phone_number()
        self.email_address = self.generate_fake_email_address(name)
        self.car = car
        self.time_licence_held = time_licence_held
    
    def __str__(self):
        print(f"{self.title} {self.first_name} {self.last_name} Info\n")
        print(f"Title: {self.title}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email Address: {self.email_address}")
        print(f"Car: {self.car.manufacturer} {self.car.model} {self.car.reg_number}\n")

    def generate_fake_phone_number(self):
        return f"07{random.randint(100000000, 999999999)}"
    

    def generate_fake_email_address(self, name) -> str:
        n = random.randint(100000, 999999)
        return f"{name[0]}{name[1]}{n}@gmail.com"

class Quote:
    def __init__(self, company, price, legal_cover, courtesy_car, breakdown_cover, windscreen_cover, personal_accident_cover):
        self.company = company
        self.price = price
        self.legal_cover = legal_cover  # feature1
        self.courtesy_car = courtesy_car  # feature2
        self.breakdown_cover = breakdown_cover  # feature3
        self.windscreen_cover = windscreen_cover  # feature4
        self.personal_accident_cover = personal_accident_cover  # feature5

# Build an attribute generator class
class AttributeGenerator:
    def __init__(self):
        self.names_by_race = {
            'South_Asian': {
                "Mr": {
                'First_Name': ['Patel', 'Singh', 'Sharma', 'Kaur', 'Ageve'],
                'Last_Name': ['Argarwal', 'Aggarwal', 'Ahluwalia', 'Ahuja', 'Akhtar']
            },
                "Miss": {
                'First_Name': ['Patel', 'Singh', 'Sharma', 'Kaur', 'Ageve'],
                'Last_Name': ['Argarwal', 'Aggarwal', 'Ahluwalia', 'Ahuja', 'Akhtar']
            }},
            'White': {
                "Mr": {
                'First_Name': ['William', 'John', 'Mark', 'Emma', 'Marie'],
                'Last_Name': ['Argarwal', 'Aggarwal', 'Ahluwalia', 'Ahuja', 'Akhtar']
            },
                "Miss": {
                'First_Name': ['Patel', 'Singh', 'Sharma', 'Kaur', 'Ageve'],
                'Last_Name': ['Argarwal', 'Aggarwal', 'Ahluwalia', 'Ahuja', 'Akhtar']
            }},
            'Black': {
                "Mr": {
                'First_Name': ['Abdu', 'Adebayo', 'Bailey', 'Carter','Imani'],
                'Last_Name': ['Butler', 'Bennet', 'Bambgbala', 'Atta', 'Carter']
            },
                "Miss": {
                'First_Name': ['Patel', 'Singh', 'Sharma', 'Kaur', 'Ageve'],
                'Last_Name': ['Argarwal', 'Aggarwal', 'Ahluwalia', 'Ahuja', 'Akhtar']
                }}
        }
        self.postcodes = ['E17AA']

    def generate_random_name(self, race) -> tuple:
        if race in self.names_by_race:
            title = random.choice(['Mr', 'Miss'])
            first_name = random.choice(self.names_by_race[race][title]['First_Name'])
            last_name = random.choice(self.names_by_race[race][title]['Last_Name'])
            return (title, first_name, last_name, race)
        else:
            raise ValueError(f"Unknown race: {race}\nOptions: {[race for race in self.names_by_race.keys()]}")

    def generate_random_birthdate(self, start_year=1960, end_year=2003) -> datetime:
        # Generate a random year, month, and day within the specified range
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        
        # Determine the last day of the month to avoid generating an invalid date
        if month in {4, 6, 9, 11}:
            day = random.randint(1, 30)
        elif month == 2:
            # Check for leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day = random.randint(1, 29)
            else:
                day = random.randint(1, 28)
        else:
            day = random.randint(1, 31)
        
        # Create a datetime object for the random birthdate
        birthdate = datetime(year, month, day)
        return birthdate
    
    def generate_random_marital_status(self) -> str:
        return random.choice(['Single', 'Married'])
    
    def generate_random_occupation_and_industry(self) -> tuple:
        tuples_of_occupations_and_industries = []
        choice = random.choice(tuples_of_occupations_and_industries)
        return choice[0], choice[1]

    def generate_random_postcode(self) -> str:
        return random.choice(self.postcodes)

