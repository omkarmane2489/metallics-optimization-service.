# metallics-optimization-service.

# Project Description 
The metallics optimizer calculates the cheapest charge mix for an electric arc furnace (EAF) in a steel plant. The charge materials are different scrap types and virgin material. In summary those materials are called commodities. The optimization algorithm uses the chemical composition of commodities as input values to guarantee that the chemical composition of the tapped melt is within a specific range. The melt is tapped after the melting process in the EAF is finished. One complete melting process as well as tapping the melt into a ladle is called a heat.

# Requirements
● The service should be implemented in Python 3.5+.
● The data should be stored in an SQL-database. You are free to choose any database management system you like.
● Please include the database initialization into the project. Use a script or data migration to fill the DB with some initial data.
● A method call should not block the service (they need to work asynchronously). We use FastAPI, but you may use any async web framework you like.
● All API methods should require user authorisation. You are free to choose any autorisation schema you want. User registration is not required, just add a user to the database when you initialize it.

# Models

There are two main models in the service: a chemical element and a commodity. </br>
1. A chemical element has the following properties:
- id - id of the element
- name - name of the element
2. Properties of a commodity are:
- id - id of the commodity
- name - name of the commodity
- inventory - current amount of the commodity on stock (in tons)
- price - current price of the commodity ($/ton)
- chemical_composition - chemical elements and their percentage in the commodity.</br>

Please notice that different commodities may have the same element in their chemical composition.</br>
Total concentration of the elements in a commodity may be below 100%. In this case, it should include a concentration of an “Unknown” element that brings the total concentration to 100%. For example, if a commodity has 15% of Cu, 25% of Al and 50% of Fe, it should also have 10% of the “Unknown” element.

# Install dependencies
Install all the dependencies from '/app/requirements.txt'

# DB initialization
Following script will create a data base with User authorization </br>
$ cd data/ <br />
$ sh db.sh

# Insert Data into DB
It will create "elements" table & insert sample data into elements table
It will also create "commodity" table and insert sample data into it. </br>
$ cd data/  <br />
$ python3 run.py

# To run the app server
Refer below steps:

$ cd app/ <br />
$ python3 run.py

# APPI ENDPOINTS

"127.0.0.1:8000/docs"
