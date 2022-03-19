from re import L
from app.db.db import DB
from fastapi import HTTPException,status

async def add_new_tag(name:str):
    if not await DB.execute('insert into tags(name) values ($1)',name):
        raise HTTPException(status_code=status.HTTP_200_OK)

async def add_tag_to_employee(tags_id: int, employee_id: int):
    if not await DB.execute('insert into tags_employee (tags_id,employee_id) values ($1,$2)',tags_id,employee_id):
        raise HTTPException(status_code=status.HTTP_200_OK)

async def remove_tag_from_employee(tags_id: int, employee_id: int):
    if not await DB.execute('delete from tags_employee where tags_id = $1 and employee_id = $2', tags_id,employee_id):
        raise HTTPException(status_code=status.HTTP_200_OK)
    
async def delete_tag(tags_id:int):
    await DB.execute('delete from tags_employee where tags_id = $1',tags_id)
    await DB.execute('delete from tags where id = $1',tags_id)

async def get_tags():
    return await DB.fetch('select id,name from tags')

async def search_by_tags(tags: list):
    return await DB.fetch('''
        with ids as 
        (select employee_id, count(tags_id)
        from tags_employee as t
        where t.tags_id = ANY($1:int[])
        group by employee_id)
        select e.id, e.name, e.surname from employee as e
        join ids on e.id = ids.employee_id
        where ids.count = $2                      
    ''',tags,len(tags))
    
async def get_tags_of_employee(employee_id: int):
    return await DB.fetch('''
        select t.id,t.name from tags_product as tp join tags on tp.tags_id = tt.id where tp.employee_id = $1                      
    ''',employee_id)
