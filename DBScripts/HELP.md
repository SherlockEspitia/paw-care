# Creacion de base de datos

Se seguiran los pasos propuestos en la siguiente guia  [Guru99](https://www.guru99.com/es/how-to-create-a-database.html)

Tambien se recomienda leer la siguiente guia [XAMPP y MYSQL](https://jhonmosquera.com/bases-de-datos-xampp/)

- Lo primero es instalar la base de datos en este caso es MYSQL [descargar](https://www.mysql.com/downloads/) buscar el instalador del [community en windows](https://dev.mysql.com/downloads/installer/) 
> [!NOTA]  
> Es importante no olvidar la contraseña de usuario root que se pone en MySQL

> [!NOTA]  
No es la version final de esta explicación

-Una vez instalado verificar que el comando mysql funcione si es asi:
Puedes usar la siguiente lista de comandos
```
$ mysql -u nom-usr -p base-dato < script.sql
```

En caso que no funcione se puede abrir la terminal de MySql X.X Command Line Interface
En donde se puede ejecutar cualquiera de los siguientes codigos:
```
source ./ruta/script.sql
-----------------
. ./ruta/script.sql
```