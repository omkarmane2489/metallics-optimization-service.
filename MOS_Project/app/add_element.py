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
        #print(element_id)

        sql_select_query = """select id,name from elements where id = %s"""
        cur.execute(sql_select_query, (element_id,))

        record = cur.fetchall()

        for row in record :
            element_data = {}

            element_data["id"] = row[0]
            #print(row[0])
            element_data["name"] = row[1]
            #print(row[1])

        element_data = json.dumps(element_data)
        print(element_data)

        # Update single record now

        sql_update_query = """Update commodity set chemical_composition = jsonb_set(chemical_composition, '{element}',(%s)) where id = %s"""

        cur.execute(sql_update_query, (element_data, _id))
        conn.commit()

        print("Updated")

    except:
        return {"Error": "Element ID is missing"}

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

    #print(commodity_data)

    chemical_composition = commodity_data["chemical_composition"]

    json_data = {}
    json_data["element"] = element_data
    json_data["percentage"] = percentage

    #print(json_data)

    chemical_composition.append(json_data)

    chemical_composition = json.dumps(chemical_composition)

    print(type(chemical_composition))



    total_percentage = 0

    for record in chemical_composition:

        print(record)

        if record["element"]["name"] != "Unknown":
            total_percentage += record["percentage"]

        if record["element"]["name"] == "Unknown":
            record["percentage"] = 100 - total_percentage

    chemical_composition = json.dumps(chemical_composition)


    # Update single record now

    sql_update_query = """Update commodity set chemical_composition = array[%s]:json[] where id = %s"""


    cur.execute(sql_update_query, (chemical_composition, _id))
    conn.commit()

    conn.close()

    return {"Status": "Added element successfully"}