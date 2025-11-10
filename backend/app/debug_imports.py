def test_imports():
    print("Probando importaciones...")
    
    try:
        from .schemas.cuidador import CuidadorResponse
        print("CuidadoResponse importado")
    except Exception as e:
        print(f"Error: {e}")
        
    try:
        from .schemas.calificacion_cuidador import CalificacionCuidadorResponse
        print("CalificacionCuidadorResponse importado")
    except Exception as e:
        print(f"Error: {e}")

test_imports()
