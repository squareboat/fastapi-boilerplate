import os

app = {
    "name": os.environ.get('APP_NAME') or "fastapi-boilerplate",
    "port": os.environ.get('APP_PORT') or 8080
}