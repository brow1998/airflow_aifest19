# Workshop Airflow - AIFEST2019

## Guia de Instalação

1. Crie seu ambiente virtual (Conda/Venv/etc)
2. `pip install -r requirements.txt`
3. `export AIRFLOW_HOME=$(pwd)`
4. `airflow initdb`
5. `airflow webserver -p 8080`
6. Em outro terminal `airflow scheduler`
7. Veja a magia acontecendo em `localhost:8080` =)