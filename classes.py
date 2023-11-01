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
    def __init__(self, company, price, legal_cover, courtesy_car, breakdown_cover, windscreen_cover, personal_accident_cover, black_box_policy, defaqto_rating, compulsory_excess):
        self.company = company
        self.price = price
        self.legal_cover = legal_cover  # feature1
        self.courtesy_car = courtesy_car  # feature2
        self.breakdown_cover = breakdown_cover  # feature3
        self.windscreen_cover = windscreen_cover  # feature4
        self.personal_accident_cover = personal_accident_cover  # feature5
        self.black_box_policy = black_box_policy
        self.defaqto_rating = defaqto_rating
        self.compulsory_excess = compulsory_excess


# Build an attribute generator class
class AttributeGenerator:
    def __init__(self):
        self.names_by_race = {
            'South_Asian': {
                "Mr": {
                    'First_Name': ['Arnav', 'Rohit', 'Vikram', 'Vignesh', 'Sanjay', 'Dinil', 'Raj', 'Dev', 'Anil', 'Ankit'],
                    'Last_Name': ['Patel', 'Shah', 'Singh', 'Khan', 'Marwaha', 'Chowdhury', 'Wickramasinghe', 'Mukherjee', 'Banerjee', 'Sinha']
                },
                "Miss": {
                    'First_Name': ['Ayesha', 'Priya', 'Pavan', 'Smita', 'Meena', 'Niranjana', 'Preeti', 'Sarika', 'Vaishnavi', 'Simran'],
                    'Last_Name': ['Patel', 'Shah', 'Singh', 'Khan', 'Marwaha', 'Chowdhury', 'Wickramasinghe', 'Mukherjee', 'Banerjee', 'Sinha']
                }},
            'White': {
                "Mr": {
                    'First_Name': ['William', 'Jonathan', 'Mark', 'James', 'Alexander', 'David', 'Thomas', 'Dominic', 'Christopher', 'Leonard'],
                    'Last_Name': ['Peters', 'Smith', 'Green', 'Brown', 'Strong', 'Cullen', 'McDermott', 'Pearson', 'Morrison', 'Baker']
                },
                "Miss": {
                    'First_Name': ['Emma', 'Isobel', 'Molly', 'Claire', 'Jossy', 'Phoebe', 'Sarah', 'Jessica', 'Holly', 'Mia'],
                    'Last_Name': ['Peters', 'Smith', 'Green', 'Brown', 'Strong', 'Cullen', 'McDermott', 'Pearson', 'Morrison', 'Baker']
                }},
            'Black': {
                "Mr": {
                    'First_Name': ['Kwame', 'Kofi', 'Kwesi', 'Ayodele', 'Chinedu', 'Osaze', 'Ade', 'Jelani', 'Amadi', 'Nana'],
                    'Last_Name': ['Nantume', 'Udemezue', 'Amenyah', 'Oluwole', 'Adeyemi', 'Okeke', 'Okafor', 'Abimbola', 'Nwosu', 'Antwi-Darkwah']
                },
                "Miss": {
                    'First_Name': ['Opeyemi', 'Agatha', 'Zainab', 'Folake', 'Chiamaka', 'Nneka', 'Yaa', 'Laila', 'Nabila', 'Amara'],
                    'Last_Name': ['Nantume', 'Udemezue', 'Amenyah', 'Oluwole', 'Adeyemi', 'Okeke', 'Okafor', 'Abimbola', 'Nwosu', 'Antwi-Darkwah']
                }}
        }

        self.postcodes = {"AW": 
                          [('B19 1QP', 'B19 3DX'), ('B19 2BB', 'B19 3DX'), ('B19 2BS', 'B18 6EX'), ('B19 2AY', 'B19 3AD'), ('B19 1QX', 'B19 3DX'), ('B19 1NP', 'B18 6EX'), ('B19 1QL', 'B19 3AD'), ('B19 1NP', 'B19 3AD'), ('B19 1QX', 'B18 6EX'), ('B19 1NP', 'B19 3DL'), ('B19 1NP', 'B18 6EL'), ('B19 2BS', 'B19 3DL'), ('B19 2HT', 'B19 3AD'), ('B19 2BS', 'B19 3AD'), ('B19 2HT', 'B18 6EX'), ('B19 1TT', 'B19 3DX'), ('B19 1QX', 'B19 3AD'), ('B19 1QX', 'B18 6EL'), ('B19 1QP', 'B19 3AD'), ('B19 2HT', 'B19 3DL'), ('B19 1NP', 'B19 3DX'), ('B19 1TT', 'B18 6EX'), ('B19 2BB', 'B19 3DL'), ('B19 1QL', 'B18 6EX'), ('B19 1TT', 'B19 3DL'), ('B19 1TT', 'B19 3AD'), ('B19 2BS', 'B19 3DX'), ('B19 2BB', 'B19 3AD'), ('B19 2AY', 'B18 6EL'), ('B19 2BZ', 'B18 6EL'), ('B19 2BS', 'B18 6EL'), ('B19 2BZ', 'B18 6EX'), ('B19 1TT', 'B18 6EL'), ('B19 2BZ', 'B19 3DL'), ('B19 1QX', 'B19 3DL'), ('B19 2AY', 'B18 6EX'), ('B19 2HT', 'B19 3DX'), ('B19 1QL', 'B19 3DX'), ('B19 1QP', 'B19 3DL'), ('B19 2BB', 'B18 6EL'), ('B19 1QL', 'B19 3DL'), ('B19 2BZ', 'B19 3AD'), ('B19 1QP', 'B18 6EL'), ('B19 2BB', 'B18 6EX'), ('B19 2AY', 'B19 3DX'), ('B19 1QL', 'B18 6EL'), ('B19 2AY', 'B19 3DL'), ('B19 2HT', 'B18 6EL'), ('B19 1QP', 'B18 6EX'), ('B19 2BZ', 'B19 3DX')],
                          "BW": 
                          [('BS2 9JU', 'BS1 6LY'), ('BS2 9JG', 'BS3 3AN'), ('B19 3BY', 'B19 3DX'), ('BS2 8XW', 'BS3 3BJ'), ('BS2 8XW', 'BS1 6AA'), ('BS2 8XQ', 'BS3 3BJ'), ('B19 2NR', 'B19 3DX'), ('SW9 8QS', 'SW9 9SA'), ('BS2 9JT', 'BS3 1ES'), ('BS2 8XQ', 'BS3 3NY'), ('BS2 8XW', 'BS3 1ES'), ('B19 3BY', 'B19 3AD'), ('B19 2SW', 'B19 3DX'), ('B19 3BX', 'B19 3DX'), ('B19 2JU', 'B18 6EL'), ('BS2 0QD', 'BS3 3AN'), ('SW9 8QS', 'SW9 8AT'), ('B19 2NY', 'B18 6EL'), ('SW9 8QT', 'SW9 9QT'), ('BS2 8XQ', 'BS1 6AA'), ('B19 3UY', 'B19 3AD'), ('B19 3BB', 'B19 3DL'), ('B19 2NR', 'B19 3DL'), ('B19 2NR', 'B18 6EX'), ('B19 2NZ', 'B18 6EL'), ('B19 2SW', 'B19 3AD'), ('B19 3BB', 'B18 6EL'), ('BS2 9JT', 'BS1 6LY'), ('B19 2NQ', 'B19 3DL'), ('B19 3BA', 'B19 3DX'), ('B19 2JU', 'B19 3DL'), ('BS2 0QD', 'BS1 6JQ'), ('BS2 8XW', 'BS3 3NY'), ('BS2 0QD', 'BS3 3BL'), ('BS2 9JU', 'BS3 1ES'), ('BS2 8XW', 'BS1 6LY'), ('B19 2NY', 'B19 3DL'), ('B19 2SW', 'B18 6EX'), ('BS2 0QD', 'BS1 6LY'), ('B19 2JU', 'B19 3AD'), ('BS2 9JG', 'BS3 3BJ'), ('BS2 9JG', 'BS1 6JQ'), ('B19 3UY', 'B18 6EX'), ('B19 3UY', 'B18 6EL'), ('B19 3BB', 'B18 6EX'), ('B19 3BA', 'B18 6EX'), ('B19 2NZ', 'B19 3DL'), ('B19 2QB', 'B18 6EL'), ('SW9 8QS', 'SW9 8BH'), ('B19 3UY', 'B19 3DL')], 
                          "AB": 
                          [('B19 2BB', 'B19 3BA'), ('B19 2BZ', 'B19 2JU'), ('B19 2BS', 'B19 2QB'), ('B19 1QL', 'B19 3BS'), ('B19 2BB', 'B19 2NQ'), ('B19 2BS', 'B19 2NY'), ('B19 2BB', 'B19 3UY'), ('B19 2HT', 'B19 3BA'), ('B19 2BS', 'B19 3BY'), ('B19 1QX', 'B19 2NR'), ('B19 1QX', 'B19 2NY'), ('B19 2BS', 'B19 3BS'), ('B19 1QP', 'B19 2QB'), ('B19 2HT', 'B19 3UY'), ('B19 1QX', 'B19 3BS'), ('B19 2BZ', 'B19 3BX'), ('B19 2AY', 'B19 3BY'), ('B19 1QX', 'B19 3BB'), ('B19 1TT', 'B19 2QB'), ('B19 2HT', 'B19 2NQ'), ('B19 1QL', 'B19 3BA'), ('B19 2BS', 'B19 3BA'), ('B19 2BZ', 'B19 2NQ'), ('B19 1QL', 'B19 2NZ'), ('B19 1NP', 'B19 2NY'), ('B19 1QP', 'B19 3BS'), ('B19 2AY', 'B19 2JU'), ('B19 1QP', 'B19 2JU'), ('B19 1QL', 'B19 2NR'), ('B19 2BZ', 'B19 2QB'), ('B19 1QX', 'B19 3UY'), ('B19 1TT', 'B19 2NZ'), ('B19 1QP', 'B19 2NY'), ('B19 1QP', 'B19 3BB'), ('B19 1QX', 'B19 3BX'), ('B19 1QX', 'B19 2SW'), ('B19 2AY', 'B19 3BX'), ('B19 1QP', 'B19 3BA'), ('B19 2BS', 'B19 3BB'), ('B19 1QX', 'B19 3BA'), ('B19 1QL', 'B19 2NY'), ('B19 2BZ', 'B19 2NZ'), ('B19 2HT', 'B19 2NR'), ('B19 1QX', 'B19 2QB'), ('B19 2HT', 'B19 3BS'), ('B19 1NP', 'B19 3BA'), ('B19 2BS', 'B19 2NQ'), ('B19 1QP', 'B19 3BX'), ('B19 1NP', 'B19 2NR'), ('B19 2HT', 'B19 2NY')]}

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
        if race_combination in self.postcodes:
            postcode_pair = random.choice(self.postcodes[race_combination])
            return postcode_pair
        else:
            raise ValueError(f"Unknown race_combination: {race_combination}\nOptions: 'BW', 'AW', 'AB'")
