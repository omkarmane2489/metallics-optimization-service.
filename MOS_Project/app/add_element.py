from app.connect_db import connect_db
import json

def add_data(data):
    conn = connect_db()
    cur = conn.cursor()

    data = json.loads(data)
    #print(data)

    try:
        _id = data["id"]
        #print(commodity_id)

    except:
        return {"Error": "Commodity ID is missing"}

    try:
        element_id = data["element_id"]

    except:
        return {"Error": "Element ID is missing"}

    sql_select_query = """select id,name from elements where id = %s"""
    cur.execute(sql_select_query, (element_id,))

    record = cur.fetchall()

    for row in record :
        element_data = {}

        element_data["id"] = row[0]
        element_data["name"] = row[1]


    try:
        percentage = data["percentage"]

    except:
        return {"Error": "percentage value is missing"}


    sql_select_query = """select * from commodity where id = %s"""
    cur.execute(sql_select_query, (_id,))

    record = cur.fetchall()

    for row in record:
        commodity_data = {}

        commodity_data["id"] = row[0]
        commodity_data["name"] = row[1]
        commodity_data["price"] = row[2]
        commodity_data["inventory"] = row[3]
        commodity_data["chemical_composition"] = row[4]


    chemical_composition = commodity_data["chemical_composition"]


    json_data = {}
    json_data["element"] = element_data
    json_data["percentage"] = percentage


    chemical_composition.append(json_data)

    total_percentage = 0

    # Calculate total percentage of all elements apart from "Unknown" element
    for record in chemical_composition:

        if record["element"]["name"] != 'Unknown':
            total_percentage += record["percentage"]

    # To calculate % of Unknown element
    for record in chemical_composition:

        if record["element"]["name"] == 'Unknown':
            record["percentage"] = 100 - total_percentage

    chemical_composition = json.dumps(chemical_composition)


    # Update single record now
    sql_update_query = """Update commodity set chemical_composition = %s where id = %s"""

    cur.execute(sql_update_query, (chemical_composition, _id))
    conn.commit()

    conn.close()

    return {"Status": "Added element successfully"}