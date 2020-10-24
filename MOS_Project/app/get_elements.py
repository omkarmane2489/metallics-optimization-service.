import psycopg2
import json
from app.connect_db import connect_db



def get_data():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT id, name from elements")

    rows = cur.fetchall()

    data = []

    for row in rows:
        element_data = {}
        #print(row[0])
        #print(row[1])
        element_data["id"] = row[0]
        element_data["name"] = row[1]

        data.append(element_data)

    #print(data)

    conn.close()

    return (data)

