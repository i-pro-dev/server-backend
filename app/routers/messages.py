from http.client import HTTPException
import re
from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
import app.queries.messages as messages_queries
import requests
from typing import Optional
from app.formatter import format_records

messages_router = APIRouter()

@messages_router.get('/messages')
async def get_user_by_id(from_user_id:int, to_user_id:int):
    result = await messages_queries.get_messages(from_user_id, to_user_id)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':{ # message,from_user_id,to_user_id,sended
            'message': result['message'],
            'from_user_id': result['from_user_id'],
            'to_user_id': result['to_user_id'],
            'sended': str(result['sended'])},
    })

@messages_router.post('/messages')
async def make_user_employee(from_user_id:int, to_user_id:int, message: str):
    await messages_queries.send_message(from_user_id, to_user_id, message)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':'Successful',
    })
    
    