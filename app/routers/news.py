from http.client import HTTPException
from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
import app.queries.messages as messages_queries
import requests
from typing import Optional
from app.formatter import format_records
from ParseTest.parseYandex import search

messages_router = APIRouter()

@messages_router.get('/news')
async def get_user_by_id(search_query: str = Query(None)):
    result = search(search_query, 'yandex.ru')
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':result,
    })
    
