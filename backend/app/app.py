from fastapi import FastAPI
from db.connection import session

app = FastAPI()

@app.get("/")
async def root():
    
    return {'message': 'Hola, Bienvenido a Paw Care'}
