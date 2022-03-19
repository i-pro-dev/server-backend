from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.routers.test import test_router
from app.routers.github import github_router
from app.db.db import DB

app = FastAPI(title='hackaton-backend')

@app.on_event('startup')
async def startup():
    await DB.connect_db()
    print('db connected')


@app.on_event('shutdown')
async def shutdown():
    await DB.disconnect_db()
    print('db disconnected')
    

app.include_router(test_router)
app.include_router(github_router)