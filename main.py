from glob import glob
import uvicorn
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from config import resolve

if __name__ == '__main__':
    uvicorn.run('apps.jobs.app:app', host='localhost', port=resolve('app.port'), reload=True)