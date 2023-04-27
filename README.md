# fast-api-prices


# Como correr la aplicacion de forma local:

 - Crear un entorno virtual python -m venv env
 - Acceder al entorno virtual 
    - Mac o Linux source env/bin/activate
    - Windows cd env/scripts activate
 - Regresar al path origen en caso de windows cd .. cd ..
 - Instalar dependecias pip install - r requierements.txt
 - Probar la aplicacion localmente uvicorn main:app --host 0.0.0.0
 - Ingresar a la ruta especificada en la terminal

# Como correr la aplicacion usando un docker container

   - Construir la imagen: docker build -t myimage .
   - Para ver las imagenes: docker images
   -  
