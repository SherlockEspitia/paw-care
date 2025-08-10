from utils.settings import Settings
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, sessionmaker
from models import Base

#settings(Settings):_Las configuraciones de la app
settings = Settings()
#Configuracion que tiene un string con todas la variables necesarias para iniciar una conexion de base de datos
URL_CONN = settings.db_conn 
    
class DBSession:
    '''
    Clase DBSession que representa la conexion a una base de datos
    
    Atributos:
        url (str): Url o Uri que sirve para relacionar la base datos a conectar
        engine: objeto que se crea con la url y sirve para sostener la conexion y sus funcionalidades
        Session: es un objeto que para crear una conexion con la base de datos y hacer uso de sus funcionalidades
        
    Metodos:
        execute_query(query): convierte una peticion sql usado en una variable que se puede usar como codigo python
        add_record(recoord): al ingresar un record este hace una transaccion con la base de datos
        query_all(model): crea un objeto de python con todos los Campos de model  
    '''
    def __init__(self, url):
        '''
        Inicializa la clase DBSession
        
        Atributos:
            url(str): url compuesta por el motor el conector, el usario, el password, 
            donde se aloja la base de datos, y la base de datos.
            engine(Engine): Clase engine de SQLAlchemy
            Session(Session): Clase session del Orm de SQLAlchemy
        '''
        self.url = url
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine) # Crea las tablas si no existen
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def get_session(self):
        return self.SessionLocal()
    
    def execute_query(self, query):
        '''
        Ejecuta una consulta de SQL
        
        Argumentos:
            query(str): consulta sql que contenga informacion posible de la base de datos
        Retorna:
            sequence[Row]: result.fetchall() es una funcion que devuelve todo los Campos de una tabla
        '''
        with self.SessionLocal() as session:
            result = session.execute(query)
            return result.fetchall()
    
    def add_record(self, record):
        '''
        Inserta todo los Campos que se agreguen a la base de datos
        
        Argumentos:
            record(Model): un registro preparado bajo un modelo de SQLAlchemy
        
        Retorna:
            None: al ser un cambio sobre la base de datos no retorna nada 
        '''
        with self.SessionLocal() as session:
            session.add(record)
            session.commit()
    
    def query_all(self, model):
        '''
        Devuelve todos los Campos que estan en un modelo
        
        Argumentos:
            model(Model): nombre del modelo SQLAlchemy
        
        Retorna:
            result(Lista): Una lista con todos Campos de la base de datos
        '''
        with self.SessionLocal() as session:
            result = session.query(model).all()
            return result
        
db_session = DBSession(URL_CONN)

# Sirve para visualizar todas las tablas que estan presentes en la base de datos
metadata = MetaData()
#metadata.reflect(session.engine)

#for t in metadata.tables:
#    print(t)

def get_db():
    session = db_session.get_session()
    try:
       yield session
    finally:
        session.close()