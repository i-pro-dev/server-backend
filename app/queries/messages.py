from app.db.db import DB
from fastapi import HTTPException,status

async def send_message(from_user_id: int, to_user_id: int, message: str):
    if not await DB.execute('insert into messages(from_user_id,to_user_id,message) values ($1,$2,$3)',from_user_id,to_user_id,message):
       HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
async def get_messages(from_user_id:int, to_user_id:int):
    return await DB.fetch('select message,from_user_id,to_user_id from messages where from_user_id = $1 and to_user_id = $2 or from_user_id = $2 and to_user_id = $1 order by id', from_user_id, to_user_id)
