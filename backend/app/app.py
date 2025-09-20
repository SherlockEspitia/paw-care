from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import propietario, cuidador

prefix = "/api/v1"

app = FastAPI(
    title= "ApPet API",
    description= "Sistema de gestion para servicios relacionados con el bienestrar de mascotas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "With ❤️ for Checho Cano and Sherlock Espitia",
        "email": "sherlockespitia@gmail.com"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(propietario.router, prefix=prefix)
app.include_router(cuidador.router, prefix=prefix)

@app.get("/", tags=["Root", "Inicio"])
async def root():
    
    return {
        'message': 'Hola, Bienvenido a ApPet',
        'docs': '/docs',
        'status': 'running'
    }

@app.get('/health', tags=["Health", "Rendimiento"])
async def health_check():
    return {"status":"healthy", "service":"ApPet"}