from classes import AttributeGenerator, Person, Car


def create_people(num_of_iterations, cars) -> list:
    generator = AttributeGenerator()
    people = []
    for car in cars:
        for _ in range(num_of_iterations):
            dob = generator.generate_random_birthdate()
            postcode = generator.generate_random_postcode()
            person_black = Person(name=generator.generate_random_name('Black'), dob=dob, postcode=postcode, car=car)
            people.append(person_black)
            person_white = Person(name=generator.generate_random_name('White'), dob=dob, postcode=postcode, car=car)
            people.append(person_white)
            person_south_asian = Person(name=generator.generate_random_name('South_Asian'), dob=dob, postcode=postcode, car=car)
            people.append(person_south_asian)
            print(person_black.__str__())
    return people

def create_cars() -> list:
    cars = []
    car = Car("Honda", "Civic", "BF14MVM")
    cars.append(car)
    return cars