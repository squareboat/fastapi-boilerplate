import uvicorn
from config import resolve
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    uvicorn.run('apps.users.app:app', host='localhost', port=resolve('app.port'), reload=True)