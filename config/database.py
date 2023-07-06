import os

db = {
    "driver": os.environ.get('DB_DRIVER'),
    "user": os.environ.get('DB_USER'),
    "password": os.environ.get('DB_PASSWORD'),
    "host": os.environ.get('DB_HOST'),
    "port": os.environ.get('DB_PORT'),
    "name": os.environ.get('DB_NAME'),
}
