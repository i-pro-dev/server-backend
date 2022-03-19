from cgitb import reset
from http.client import HTTPException
from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
import app.queries.tags as tags_queries
import requests
from typing import Optional,List
from app.formatter import format_record, format_records

tags_router = APIRouter()

@tags_router.post('/tag')
async def add_new_tag(tag_name: int):
    await tags_queries.add_new_tag(tag_name)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':'Successful',
    })
    
@tags_router.post('/user/tag')
async def add_tag_to_employee(tags_id: int, employee_id: int):
    await tags_queries.add_new_tag(tags_id,employee_id)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details': 'Successful',
    })

@tags_router.delete('/user/tag')
async def remove_tag_from_employee(tags_id:int, employee_id:int):
    await tags_queries.remove_tag_from_employee(tags_id,employee_id)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':'Successful',
    })
    
@tags_router.delete('/tag')
async def delete_tag(tags_id: int):
    await tags_queries.delete_tag(tags_id)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':'Successful',
    })

@tags_router.get('/tags')
async def get_tags():
    result = await tags_queries.get_tags()
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':format_records(result),
    })
    
@tags_router.get('/tags/users')
async def search_by_tags(tags:List[str]):
    result = await tags_queries.search_by_tags(tags)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':format_records(result),
    })

@tags_router.get('/user/{user_id}/tags')
async def get_tags_of_employee(employee_id: int):
    result = await tags_queries.get_tags_of_employee(employee_id)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':format_records(result),
    })
