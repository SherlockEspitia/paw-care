# Api Rest para ApPet

ApPet es un servicio que permite ubicar los mejores servicios para el cuidado de tu mascota

## Aspectos Tecnicos

Recuerde que este es un sistema destribuido por lo cual se tienen dos softwares separados uno que ejecuta toda la logica del negocio y otro que efectua la interacion con el usuario. En la presente lectura todo se refiere al uso de la logica del negocio, por lo cual lo ideal es navegar al directorio llamado backend.
```cd backend```

Para iniciar la ApiRest segun tu ventana de comandos iniciar primero el entorno virtual de la siguiente manera:
```bash source env/Scripts/activate```
o en Windows
```cmd env\Scripts\activate.bat``` o ```PowerShell env\Scripts\Activate.ps1```

Luego navegar a la carpeta app
```cd app```

luego en esta carpeta se puede visualizar todos los artefactos necesarios para iniciar la API de la siguiente manera
```fastapi dev app.py```
tambien se puede dejar el modo escucha activado para trabajar sobre cuando se esta probando la API con el siguiente comando
```python -m uvicorn app:app --reload```
este comando se debe ejecutar sobre la raiz del proyecto en este caso el backend
```$ python -m uvicorn app.app:app --reload```

Una vez inicia la ApiRest se podra navegar a el mediante la url <http://127.0.0.1:8000></br>
Y sera visible un mensaje de bienvenida y en la url <http://127.0.0.1:8000/docs>
