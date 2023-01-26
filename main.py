import uvicorn

if __name__ == '__main__':
    uvicorn.run('apps.users.app:app', host='localhost', port=8080)