from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    
    return {'message': 'Hola, Bienvenido a Paw Care'}
