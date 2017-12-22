https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/


# Setup
- virtualenv .env
- pip3 install --upgrade -r requirements.txt

- install Postgres CLI
- psql
- [create wordarithmetic_dev;]
- [\q]
- export DATABASE_URL="postgresql://localhost/wordarithmetic_dev"
- export APP_SETTINGS="config.DevelopmentConfig"

- python3 manage.py db init
- python3 manage.py db migrate
- python3 manage.py db upgrade

## Read DB
- psql
- [\c wordcount_dev]
- [\dt ]
- [\d Equation]
