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
        self.black_white_postcodes=[
    ('B19 3UY', 'B18 6EX'), ('B6 4HA', 'B19 3DL'), ('B19 3BA', 'B19 3DX'), ('B19 3BB', 'B19 3AD'), 
    ('B19 3BS', 'B18 6EL'), 
    ('SE24 0LP','SW9 8BH'), ('SW9 8QS', 'SW9 9SA'), ('SW9 8QR', 'SW9 8AT'), ('SW2 1EH', 'SW9 9UP'), 
    ('SW9 8QT', 'SW9 9QT'), 
    ('M16 7LR', 'M40 3PT'), ('M14 4SX', 'M40 3QT'), ('M16 7LA', 'M40 3QX'), ('M14 4SS', 'M40 3SS'), 
    ('M16 7LN', 'M40 3QE'), 
    ('M14 4RE', 'M40 3WA'), ('M14 4JR', 'M40 3WN'), ('M14 4SA', 'M40 3ND'), ('M14 4JQ', 'M40 0BX'),
    ('M14 4WE', 'M40 3NW'),
    ('B19 3BX', 'B32 3AU'), ('B19 2NQ', 'B29 5PQ'), ('B19 2NR', 'B29 5TX'), ('B19 3BY', 'B31 1XN'), 
    ('B19 2JU', 'B31 1AH'), 
    ('B6 4JX', 'B44 0AZ'), ('B19 2QB', 'B23 5DE'), ('B19 2NZ', 'B23 5XL'), ('B19 2NY', 'B23 5AT'),
    ('B19 2SW', 'B23 5XN'),
    ('B7 4ET', 'B31 3UJ'), ('B7 4SA', 'B31 3UG'), ('B7 4QP', 'B31 3AA'), ('B7 4AH', 'B31 3AB'), 
    ('B7 4SH', 'B31 2NB'),
    ('BS2 0QD', 'BS7 0BD'), ('BS5 9SJ', 'BS7 0EU'), ('BS5 9SX', 'BS7 0EW'), ('BS5 9ST', 'BS7 0LE'),
    ('BS5 9SR', 'BS7 0EQ'), 
    ('BS2 8XQ', 'BS3 1ES'), ('BS2 8XW', 'BS3 3NY'),('BS2 9JG', 'BS3 3AN'), ('BS2 9JT', 'BS3 3BL'),
    ('BS2 9JU', 'BS3 3BJ'),
    ('B7 5AS', 'B24 9ES'), ('B7 5ET', 'B23 6GR'), ('B7 5AB', 'B24 9HE'), ('B7 4QJ', 'B24 9DW'), 
    ('B7 5JD', 'B24 9HB'), 
    ('B7 5BP', 'B15 3AS'), ('B7 5BQ', 'B15 2LB'), ('B7 5BD', 'B15 3SS'), ('B7 5BW', 'B15 2JR'),
    ('B7 5BJ', 'B15 2LL')
    ]
        self.asian_white_postcodes = [
    ('LE4 7QA', 'LE4 2JN'), ('LE4 7SB', 'LE4 2RJ'), ('LE4 7QZ',
                                                     'LE4 2QF'), ('LE4 5PN', 'LE4 2PW'),
    ('LE4 7PR', 'LE4 2PE'),
    ('OL1 2EE', 'OL1 3HY'), ('OL1 2EL', 'OL1 3RH'), ('OL9 6AX',
                                                     'OL1 3UX'), ('OL1 2NL', 'OL1 3QW'),
    ('OL1 2NJ', 'OL1 3RS'),
    ('BB1 5PA', 'BB1 4EL'), ('BB1 5QB', 'BB1 4BH'), ('BB1 5LB',
                                                     'BB5 4LS'), ('BB1 5FB', 'BB1 4BY'),
    ('BB1 3AB', 'BB1 4AH'),
    ('B19 1TT', 'B32 3EN'), ('B19 1QP', 'B32 3HU'), ('B19 1QX',
                                                     'B32 3DL'), ('B19 1NP', 'B32 3DB'),
    ('B19 1QL', 'B32 3HR'),
    ('B19 2BB', 'B32 3BS'), ('B19 2HT', 'B32 3BL'), ('B19 2BZ',
                                                     'B62 0QD'), ('B19 2AY', 'B32 3QR'),
    ('B19 2BS', 'B62 0EP'),
    ('BD7 3AU', 'WS3 1DW'), ('BD7 2BY', 'WS3 1DF'), ('BD7 2BL',
                                                     'WS3 1DL'), ('BD7 3AG', 'WS3 1FQ'),
    ('BD7 2BU', 'WS3 1PD'),
    ('BD7 3AN', 'BS1 6LY'), ('BD7 2DQ', 'BS1 6HH'), ('BD7 3AA',
                                                     'BS1 6JQ'), ('BD7 3AL', 'BS1 6BA'),
    ('BD7 2DW', 'BS1 6AA'),
    ('LE4 5HS', 'LE11 2JS'), ('LE4 5HZ', 'LE11 2JW'), ('LE4 5HH',
                                                       'LE11 2LN'), ('LE4 5BB', 'LE11 2JD'),
    ('LE4 5GG', 'LE11 2NA'),
    ('LE4 5FG', 'LE11 2DQ'), ('LE4 5AW', 'LE11 2QR'), ('LE4 5HP',
                                                       'LE11 2QS'), ('LE4 5GF', 'LE11 2NL'),
    ('LE4 5GZ', 'LE11 2FD'),
    ('OL8 1UQ', 'DN1 2LT'), ('OL8 1TU', 'DN1 2EU'), ('OL8 1TH',
                                                     'DN1 2ES'), ('OL9 6HA', 'DN1 2NB'),
    ('OL8 1TP', 'DN1 2NN'),
    ('OL12 9BL', 'DN1 2JG'), ('OL12 9BQ',
                              'DN1 2NA'), ('OL16 2LE', 'DN1 2HY'), ('OL16 2NA', 'DN1 2HU'),
    ('OL16 2DS', 'DN1 2NE'),
    ('BB5 1SP', 'DY11 7DR'), ('BB5 1SZ', 'DY11 7BW'), ('BB5 1SS',
                                                       'DY11 7JD'), ('BB5 1TG', 'DY11 7BF'),
    ('BB5 1TD', 'DY11 7DS'),
    ('B11 3LG', 'B45 0BQ'), ('B11 3NN', 'B45 0LD'), ('B11 3TA',
                                                     'B45 0DE'), ('B11 4AW', 'B45 0HB'),
    ('B11 3LE', 'B45 0BH')
]

    def generate_random_name(self, race) -> tuple:
        if race in self.names_by_race:
            title = random.choice(['Mr', 'Miss'])
            first_name = random.choice(self.names_by_race[race][title]['First_Name'])
            last_name = random.choice(self.names_by_race[race][title]['Last_Name'])
            return (title, first_name, last_name, race)
        else:
            raise ValueError(f"Unknown race: {race}\nOptions: {[race for race in self.names_by_race.keys()]}")

    # def generate_random_birthdate(self, start_year=1960, end_year=2003) -> datetime:
    #     # Generate a random year, month, and day within the specified range
    #     year = random.randint(start_year, end_year)
    #     month = random.randint(1, 12)
        
    #     # Determine the last day of the month to avoid generating an invalid date
    #     if month in {4, 6, 9, 11}:
    #         day = random.randint(1, 30)
    #     elif month == 2:
    #         # Check for leap year
    #         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    #             day = random.randint(1, 29)
    #         else:
    #             day = random.randint(1, 28)
    #     else:
    #         day = random.randint(1, 31)
        
    #     # Create a datetime object for the random birthdate
    #     birthdate = datetime(year, month, day)
    #     return birthdate
    def select_birthdate(self) -> datetime:
        current_year = datetime.now().year
        month = 10
        day = 10
        twenty_yo = datetime(year=current_year - 20, month=month, day=day)
        thirty_five_yo = datetime(year=current_year - 35, month=month, day=day)
        fifty_five_yo = datetime(year=current_year - 55, month=month, day=day)
        ages = [twenty_yo, thirty_five_yo, fifty_five_yo]

        # Select randomly among the ages
        random_dob = random.choice(ages)

        return random_dob


    
    def generate_random_marital_status(self) -> str:
        return random.choice(['Single', 'Married'])
    
    def generate_random_occupation_and_industry(self) -> tuple:
        tuples_of_occupations_and_industries = []
        choice = random.choice(tuples_of_occupations_and_industries)
        return choice[0], choice[1]

    def generate_random_postcode(self, race_combination) -> tuple:
        if race_combination == "BW":
            return random.choice(self.black_white_postcodes)
        elif race_combination == "AW":
            return random.choice(self.asian_white_postcodes)
        else:
            raise ValueError(f"Unknown race_combination: {race_combination}\nOptions: 'BW', 'AW'")


