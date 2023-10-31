from classes import Person, Car, AttributeGenerator
from scrape import setup_webdriver, close_webdriver, scrape
from utils import create_people, create_cars
import time
from soupify import extract_quotes
from db import connect_to_database, close_database, setup_database, insert_person, insert_quotes_for_person


def main():
    rows_in_people_db = 0
    conn = connect_to_database()
    setup_database(conn)
    cars = create_cars()
    all_people = create_people(num_of_iterations=10, cars=cars)
    for person in all_people:
        ts = time.monotonic()
        try:
            driver = setup_webdriver()
            print(f'Scraping quotes for: {person.first_name} {person.last_name}')
            html = scrape(person, driver)
            quotes = extract_quotes(html=html)
            print(f'Found {len(quotes)} quotes for {person.first_name} {person.last_name}')
            close_webdriver(driver)
            person_id = insert_person(conn, person)
            insert_quotes_for_person(conn, person_id, quotes)
            rows_in_people_db += 1
        except Exception as e:
            print(e)
        finally:
            te = time.monotonic()
            tte = te - ts
            print(tte)
    close_database(conn)
    print(f'Inserted {rows_in_people_db} rows into the People table.')

if __name__ == "__main__":
    main()
    