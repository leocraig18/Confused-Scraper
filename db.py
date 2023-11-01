import sqlite3

def connect_to_database():
    conn = sqlite3.connect('insurance_data.db')
    return conn
def close_database(conn):
    conn.close()

def setup_database(conn):
    db = conn.cursor()

    # Create 'People' table (without inline SQL comments)
    db.execute('''
              CREATE TABLE IF NOT EXISTS People (
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  first_name TEXT,
                  last_name TEXT, 
                  race TEXT,           
                  dob DATETIME,  
                  postcode TEXT,
                  car_make TEXT,
                  car_model TEXT,
                  car_reg TEXT
              )
              ''')

    # Create 'Quotes' table (without inline SQL comments)
    db.execute('''
              CREATE TABLE IF NOT EXISTS Quotes (
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  person_id INTEGER,
                  company TEXT,
                  price REAL,
                  legal_cover BOOLEAN,
                  courtesy_car BOOLEAN,
                  breakdown_cover BOOLEAN,
                  windscreen_cover BOOLEAN,
                  personal_accident_cover BOOLEAN,
                  black_box_policy BOOLEAN,
                  defaqto_rating BOONLEAN,
                  compulsory_excess REAL,
                  FOREIGN KEY (person_id) REFERENCES People (ID)
              )
              ''')

    # Commit the changes and close the connection
    conn.commit()

    return "Database setup complete with 'People' and 'Quotes' tables."

def insert_person(db, person):
    """
    Insert a new person into the People table and return the new ID.
    """
    db.cursor()
    # Prepare the INSERT statement
    sql = '''
          INSERT INTO People (title, first_name, last_name, race, dob, postcode, car_make, car_model, car_reg)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
          '''
    cur = db.cursor()
    cur.execute(sql, (person.title, person.first_name, person.last_name, person.race, person.dob, person.postcode, person.car.manufacturer, person.car.model, person.car.reg_number))

    # Commit the transaction
    db.commit()

    # Retrieve the ID of the new record and return it
    return cur.lastrowid

def insert_quotes_for_person(db, person_id, quotes):
    """
    Insert quotes for a specific person into the Quotes table.
    """
    db.cursor()
    # Prepare the INSERT statement
    sql = '''
          INSERT INTO Quotes (person_id, company, price, legal_cover, courtesy_car, breakdown_cover, windscreen_cover, personal_accident_cover, black_box_policy, defaqto_rating, compulsory_excess)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
          '''

    cur = db.cursor()

    # Iterate through the quotes and insert each one with the same person_id
    for quote in quotes:
        cur.execute(sql, (person_id, quote.company, quote.price, quote.legal_cover, quote.courtesy_car, quote.breakdown_cover, quote.windscreen_cover, quote.personal_accident_cover, quote.black_box_policy, quote.defaqto_rating, quote.compulsory_excess))

    # Commit the transaction
    db.commit()

