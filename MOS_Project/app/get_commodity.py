import psycopg2
import json
from app.connect_db import connect_db


def get_commodity_data(id):

    conn = connect_db()
    cur = conn.cursor()

    try:

        sql_select_query = """select * from commodity where id = %s"""
        cur.execute(sql_select_query, (id,))

        record  = cur.fetchall()

        data = []

        for row in record :
            commodity_data = {}

            commodity_data["id"] = row[0]
            commodity_data["name"] = row[1]
            commodity_data["price"] = row[2]
            commodity_data["inventory"] = row[3]
            commodity_data["chemical_composition"] = row[4]

            data.append(commodity_data)

        #json_data = json.dumps(data)

        #print(data)
        conn.close()

        return (data)

    except Exception as e:
        return e

