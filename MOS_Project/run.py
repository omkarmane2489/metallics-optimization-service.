import uvicorn
from fastapi import FastAPI
from app.get_elements import get_data
from app.get_commodity import get_commodity_data
from app.update_commodity import update_record
from app.add_element import add_data
from app.delete_element import delete_data

app = FastAPI()


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

@app.post('/add_element/{data}')
async def add_element(data):
    a = add_data(data)
    return a

@app.post('/delete_data/{data}')
async def delete_element(data):
    a = delete_data(data)
    return a


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug = True)