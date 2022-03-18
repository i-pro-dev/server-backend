import asyncpg
from app.settings import DATABASE_URL

class DB:
    con: asyncpg.connection.Connection = None
    
    @classmethod
    async def connect_db(cls):
        try:
            cls.con = await asyncpg.connect(DATABASE_URL)
        except Exception as error:
            print(error)
            
    @classmethod
    async def disconnect_db(cls):
        await cls.con.close()
        
    @classmethod
    async def execute(cls, sql, *args):
        try:
            await DB.con.execute(sql, *args)
        except Exception as error:
            print(error)
            return False
        return True

    @classmethod
    async def fetch(cls, sql, *args):
        try:
            return await DB.con.fetch(sql, *args)
        except Exception as error:
            print(error)
            return False

    @classmethod
    async def fetchrow(cls, sql, *args):
        try:
            return await DB.con.fetchrow(sql, *args)
        except Exception as error:
            print(error)
            return False

    @classmethod
    async def fetchval(cls, sql, *args):
        try:
            return await DB.con.fetchval(sql, *args)
        except Exception as error:
            print(error)
            return False