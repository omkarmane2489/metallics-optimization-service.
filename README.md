# metallics-optimization-service.

# Project Description 
The metallics optimizer calculates the cheapest charge mix for an electric arc furnace (EAF) in a steel plant. The charge materials are different scrap types and virgin material. In summary those materials are called commodities. The optimization algorithm uses the chemical composition of commodities as input values to guarantee that the chemical composition of the tapped melt is within a specific range. The melt is tapped after the melting process in the EAF is finished. One complete melting process as well as tapping the melt into a ladle is called a heat.

# Requirements
1. Python3.5+
2. FastAPI
3. PostgreSQL

# Install dependencies
Install all the dependencies from '/app/requirements.txt'

# DB initialization
Following script will create a data base with User authorization
$ cd data/
$ sh db.sh

# Insert Data into DB
It will create "elements" table & insert sample data into elements table
It will also create "commodity" table and insert sample data into it.
$ cd data
$ python3 run.py

# To run the app server
Refer below steps:

$ cd app/
$ python3 run.py
