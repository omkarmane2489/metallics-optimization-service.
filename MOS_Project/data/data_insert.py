from app.config import *
from app.connect_db import connect_db
import json

# Function creates "Elements" table
def create_element_table():

    #Connect to DB
    conn = connect_db()

    cur = conn.cursor()


    # Create "element" table
    cur.execute('''CREATE TABLE elements
          (id INT PRIMARY KEY     NOT NULL,
          name          VARCHAR    NOT NULL
          );''')

    print("Elements table created successfully")

    conn.commit()
    conn.close()

# Function inserts elements data
def insert_element_data():

    # Connect to DB
    conn = connect_db()

    cur = conn.cursor()

    # Get sample elements data from file
    with open('elements.json') as f:
        data = json.load(f)


    for record in data:

        # Convert data into json
        record = json.dumps(record)

        # SQL query for data insertion
        sql_add_query = '''INSERT INTO elements
                        SELECT id, name
                        FROM json_populate_record(NULL::elements,
						%s)'''

        cur.execute(sql_add_query, (record,))

    conn.commit()
    conn.close()

    print("Elements data inserted")

# Function creates "Commodity" table into DB
def create_commodity_table():

    conn = connect_db()

    cur = conn.cursor()

    cur.execute('''CREATE TABLE commodity
              (id INT PRIMARY KEY     NOT NULL,
              name           VARCHAR    NOT NULL,
              price NUMERIC NOT NULL,
              inventory NUMERIC NOT NULL,
              chemical_composition JSON NOT NULL
              );''')
    print("Commodity Table created successfully")

    conn.commit()
    conn.close()

# Function inserts "Commodity" data
def insert_commodity_data():
    conn = connect_db()

    cur = conn.cursor()

    with open('commodity.json') as f:
        data = json.load(f)

    for record in data:
        #print(record)

        record = json.dumps(record)

        sql_add_query = '''INSERT INTO commodity
            SELECT id, name, price, inventory, chemical_composition
            FROM json_populate_record (NULL::commodity,
            %s)'''

        cur.execute(sql_add_query,(record,))

    conn.commit()
    conn.close()

    print("Commodity data inserted")







