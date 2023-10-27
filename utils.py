from classes import AttributeGenerator, Person, Car


def create_people(num_of_iterations, cars) -> list:
    generator = AttributeGenerator()
    people = []
    for car in cars:
        for _ in range(num_of_iterations):
            dob = generator.select_birthdate()
            postcode_bw = generator.generate_random_postcode('BW')
            postcode_aw = generator.generate_random_postcode('AW')
            person_black = Person(name=generator.generate_random_name('Black'), dob=dob, postcode=postcode_bw[0], car=car)
            people.append(person_black)
            person_white = Person(name=generator.generate_random_name('White'), dob=dob, postcode=postcode_bw[1], car=car)
            people.append(person_white)
            person_south_asian = Person(name=generator.generate_random_name('South_Asian'), dob=dob, postcode=postcode_aw[0], car=car)
            people.append(person_south_asian)
            person_white2 = Person(name=generator.generate_random_name('White'), dob=dob, postcode=postcode_aw[1], car=car)
            people.append(person_white2)
    return people

def create_cars() -> list:
    cars = []
    car = Car("Honda", "Civic", "BF14MVM")
    cars.append(car)
    car = Car("Volvo", "XC60", "SL16SCX")
    cars.append(car)
    car = Car("Mercedes-Benz", "GLC", "KW72FCO")
    cars.append(car)

    return cars