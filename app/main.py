from fastapi import FastAPI
import uvicorn
from app.endpoints.routers import main_router

app = FastAPI()

app.include_router(main_router)



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, env_file='/.env')

    # uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level="info",reload=True)
