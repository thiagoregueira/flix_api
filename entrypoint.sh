#!/bin/bash
set -e

echo "Aplicando migrações..."
python manage.py migrate

echo "Carregando dados iniciais..."
python manage.py loaddata initial_data.json || echo "Aviso: Falha ao carregar initial_data.json. Talvez os dados já existam."

echo "Garantindo superusuário..."
python create_superuser.py || echo "Aviso: Falha ao criar superusuário."

echo "Iniciando servidor com Gunicorn..."
exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3
