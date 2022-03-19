import imp
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.routers.github import github_router
from app.routers.users import users_router
from app.routers.messages import messages_router
from app.routers.tags import tags_router
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
    

app.include_router(github_router)
app.include_router(users_router)
app.include_router(messages_router)
app.include_router(tags_router)