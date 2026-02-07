#!/bin/bash
set -e

# Rodar migrações
python manage.py migrate

# Tentar carregar dados iniciais só se o usuário pedir ou se o banco parecer vazio 
# (simples tentaiva, se falhar, continua)
python manage.py loaddata initial_data.json || echo "Dados já existentes ou erro ao carregar."

# Iniciar Gunicorn
# Ajuste o número de workers conforme necessário (2 * CPU + 1)
exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3
