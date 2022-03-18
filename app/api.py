from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.routers.test import test_router

app = FastAPI(title='hackaton-backend')

@app.on_event('startup')
async def startup():
    pass


@app.on_event('shutdown')
async def shutdown():
    pass

app.include_router(test_router)