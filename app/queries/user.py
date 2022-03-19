from app.db.db import DB
from fastapi import HTTPException,status

async def add_user(name: str, surname: str,login: str, hashed_password: str):
    if not await DB.execute('insert into users(name,surname,login,hashed_password) values ($1,$2,$3,$4)',name,surname,login,hashed_password):
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
async def make_user_employee(user_id: int, github_url: str, github_api_key: str, google_api_key: str):
    if not await DB.execute('insert into employee_data(id,github_url,github_api_key,google_api_key) values ($1,$2,$3,$4)',user_id,github_url,github_api_key,google_api_key):
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
   
async def get_user_by_login(login: str):
    result =  await DB.fetchrow('select id,name,surname from users where login = $1', login)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return result
        
async def get_user_by_id(user_id:int):
    result =  await DB.fetchrow('select id,name,surname from users where id=$1',user_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return result
        
async def get_users():
    return await DB.fetch('select id,name,surname from users')