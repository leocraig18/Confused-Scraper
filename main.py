from classes import Person, Car, AttributeGenerator
from scrape import scrape, setup_webdriver, close_webdriver
from utils import create_people, create_cars
import time
from soupify import extract_quotes
from db import connect_to_database, close_database, setup_database, insert_person, insert_quotes_for_person


def main():
    conn = connect_to_database()
    setup_database(conn)
    cars = create_cars()
    all_people = create_people(num_of_iterations=3, cars=cars)
    for person in all_people:
        driver = setup_webdriver()
        print(f'Scraping quotes for: {person.first_name} {person.last_name}')
        html = scrape(person, driver)
        quotes = extract_quotes(html=html)
        print(f'Found {len(quotes)} quotes for {person.first_name} {person.last_name}')
        close_webdriver(driver)
        person_id = insert_person(conn, person)
        insert_quotes_for_person(conn, person_id, quotes)
    close_database(conn)
if __name__ == "__main__":
    main()

# Build a function that builds database that has two tables one called people the other quotes if it isnt already created. There should be a 1 to many relationship between a person and many quotes. And then build a function that takes the quotes and the person in question and adds them to the database. Each of the quotes in one iteration should of course have the same person_id as their foreign key to connect them all to the same person.
