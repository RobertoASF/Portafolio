# Instalacion de TindPlace, proyecto con Django y Postgres utilizado con Docker Compose

Este archivo README.md tiene como objetivo proporcionar las instrucciones necesarias para clonar un repositorio de Github que contiene un proyecto Django y una base de datos Postgres que se utilizan con Docker Compose.

## Requisitos del sistema

Para poder correr este proyecto necesitarás contar con lo siguiente:

* Docker 
* Docker Compose
* Git 

## Para clonar el repositorio

1. Abre una terminal en tu sistema operativo y navega hasta el directorio donde deseas clonar el repositorio.
2. Ejecuta el siguiente comando para clonar el repositorio:

```bash
git clone https://github.com/RobertoASF/Portafolio.git 
```

3. Espera a que el proceso de clonación termine. Una vez finalizado, tendrás una copia del repositorio en tu sistema.

## Uso del proyecto Django con Docker Compose

Antes de ejecutar `docker-compose up`, se recomienda realizar un `prune` para eliminar posibles contenedores, redes y volúmenes no utilizados. Sigue estos pasos:

1. En la terminal, navega hasta el directorio raíz del proyecto Django.
2. Ejecuta el siguiente comando para eliminar los contenedores, redes y volúmenes no utilizados:

```bash
docker system prune -a
```


Este comando eliminará los contenedores, redes y volúmenes no utilizados.

3. Ejecuta el siguiente comando para construir las imágenes de Docker:

```bash
docker-compose build --no-cache
```

Este comando creará las imágenes de Docker necesarias para el proyecto.

4. Ejecuta el siguiente comando para iniciar el proyecto:

```bash
docker-compose up -d
```

Este comando iniciará el proyecto Django y la base de datos Postgres en contenedores de Docker en modo detach.

5. Abre tu navegador web y navega hasta [http://localhost:8000](http://localhost:8000) para acceder a la página de inicio del proyecto Django. Si todo funciona correctamente, deberías ver la página de inicio de TindPlace.

6. Cuando hayas terminado de trabajar con el proyecto, puedes detener los contenedores de Docker con el siguiente comando:
```bash
docker-compose down
```


Este comando detendrá los contenedores de Docker y eliminará los contenedores, las redes y los volúmenes creados por Docker Compose.


## Resolución de problemas

* En caso de usar sistemas Linux o MAC es posbile que los comandos `docker-compose build` , `docker-compose up` , `docker-compose down` y `docker system prune` es posible que se requieran permisos de administrador, por lo que se recomienda ejecutarlos como súper usuario usando `sudo`.

* En caso de usuarios Linux, especialemnte las basadas en RedHat es posbile que el servicio SELinux genere problemas al desplegar la aplicación, por lo que se recomienda desactivarlo temporalmente con el siguiente comando: 
```sh
  sudo setenforce 0
  ```
* En caso de que al ejecutar `docker-compose up` obtener mensaje de error que no se tienen los permisos para ejecutar el archivo manage.py ejecutar el siguiente comando
```bash
chmod +rx /ruta/al/archivo/manage.py
```



