#!/bin/sh

#echo 'Running collecstatic...'
#python manage.py collectstatic --no-input --settings=config.settings.production

#echo 'Applying migrations...'
#python manage.py wait_for_db --settings=config.settings.production
#python manage.py migrate --settings=config.settings.production

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.production config.wsgi:application --bind 0.0.0.0:8000

echo 'Poblando base de datos'

# Variables de conexión a la base de datos
HOST="tindplace-db"
DBNAME="tindplace"
USER="admin"
PASSWORD="portafolio"

# Ejecuta creación de tablas
echo "Ejecutando mod_database.sql ..."
psql -h $HOST -d $DBNAME -U $USER -W $PASSWORD -f mod_database.sql

# Ejecuta poblado de tablas
echo "Ejecutando pobla_db.sql ..."
psql -h $HOST -d $DBNAME -U $USER -W $PASSWORD -f pobla_db.sql
