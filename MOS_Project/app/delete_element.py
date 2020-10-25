import psycopg2
from app.connect_db import connect_db
from fastapi.responses import JSONResponse

import json
def delete_data(data):

    conn = connect_db()
    cur = conn.cursor()

    data = json.loads(data)
    # print(data)

    try:
        _id = data["id"]
        # print(commodity_id)

    except:
        return {"Error": "Commodity ID is missing"}

    try:
        element_id = data["element_id"]

    except:
        return {"Error": "Element ID is missing"}

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

    updated_list = []
    total_percentage = 0

    for record in chemical_composition:

        if record["element"]["id"] != element_id:
            updated_list.append(record)
            total_percentage += record["percentage"]


        if record["element"]["name"] == "Unknown":
            record["percentage"] += (100 -total_percentage)


    updated_composition = json.dumps(updated_list)

    # Update single record now
    sql_update_query = """Update commodity set chemical_composition = %s where id = %s"""

    cur.execute(sql_update_query, (updated_composition, _id))
    conn.commit()

    conn.close()

    return {"Status": "Element deleted successfully"}
