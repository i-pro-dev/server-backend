from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

test_router = APIRouter(tags=['test'])

@test_router.get('/test')
async def test():
    return JSONResponse(status_code=status.HTTP_200_OK,
        content={'details':'Executed'}                    
    )