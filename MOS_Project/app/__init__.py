from fastapi import FastAPI
from app.get_elements import get_data
from app.get_commodity import get_commodity_data
from app.update_commodity import update_record

app = FastAPI()


'''@app.get("/")
async def read_root():
    return {"Hello": "World"}'''

@app.get('/elements')
async def get_elemants():
    a = get_data()
    return a

@app.get('/commodity/{id}')
async def get_commodity(id):
    a = get_commodity_data(id)
    return a

@app.post('/update_commodity/{data}')
async def update_commodity(data):
    a = update_record(data)
    return a
