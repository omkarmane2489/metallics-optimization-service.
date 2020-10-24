import psycopg2
from app.connect_db import connect_db
from fastapi.responses import JSONResponse

import json

def update_record(data):

    conn = connect_db()
    cur = conn.cursor()

    data = json.loads(data)

    #print(data)

    #print(data["id"])

    try:
        _id = data["id"]
        #print(id)

    except:
        return {"Error: ID is missing"}

    key_list = list(data.keys())

    #print(key_list)


    if 'name' in key_list:
        name = data["name"]
        # Update single record now
        sql_update_query = """Update commodity set name = %s where id = %s"""
        cur.execute(sql_update_query, (name, _id))
        conn.commit()
        count = cur.rowcount
        #print(count, "Record Updated successfully ")


    if 'price' in key_list:
        price = data['price']
        # Update single record now
        sql_update_query = """Update commodity set price = %s where id = %s"""
        cur.execute(sql_update_query, (price, _id))
        conn.commit()
        count = cur.rowcount



    if 'inventory' in key_list:
        inventory = data["inventory"]
        # Update single record now
        sql_update_query = """Update commodity set inventory = %s where id = %s"""
        cur.execute(sql_update_query, (inventory, _id))
        conn.commit()
        count = cur.rowcount
        #print(count, "Record Updated successfully ")


    conn.close()

    return {"status": "Record updated successfully"}

