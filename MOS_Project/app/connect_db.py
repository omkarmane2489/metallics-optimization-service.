import psycopg2
from app.config import *

def connect_db():

    conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

    return conn

