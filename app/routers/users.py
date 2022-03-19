from http.client import HTTPException
from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
import app.queries.user as user_queries
import requests
from typing import Optional
from app.formatter import format_record, format_records

users_router = APIRouter()

@users_router.get('/user/{user_id}')
async def get_user_by_id(user_id: int):
    result = await user_queries.get_user_by_id(user_id)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':result,
    })
    
@users_router.get('/user')
async def get_user_by_login(login: str):
    result = await user_queries.get_user_by_login(login)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details': format_record(result),
    })

@users_router.get('/users')
async def get_users():
    result = await user_queries.get_users()
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':format_records(result),
    })
    
@users_router.post('/user')
async def add_user(name: str, surname: str,login: str, hashed_password: str):
    await user_queries.add_user(name, surname,login, hashed_password)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':'Successful',
    })

@users_router.post('/user/{user_id}/employee')
async def make_user_employee(user_id: int, github_url: str, github_api_key: str,google_api_key: str):
    await user_queries.make_user_employee(user_id, github_url, github_api_key,google_api_key)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':'Successful',
    })
    
    