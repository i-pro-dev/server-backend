from http.client import HTTPException
from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
import requests
from typing import Optional

github_router = APIRouter()

@github_router.get('/github')
async def get_github_info(github_name: str, github_token: Optional[str] = None):
    if not github_token:
        pass
    url = f'https://api.github.com/users/{github_name}'
    result = requests.get(url,headers={'Authorization': 'token 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'})
    if result.status_code != 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    result = result.json()
    
    user = {
        'name' : github_name,
    }
    try:
        user['total_repos'] = 0
        user['total_repos'] += result['public_repos'] 
        user['total_repos'] += result['total_private_repos']
    except Exception as er:
        print(er)
    try:
        user['pro'] = result['plan']['name'] == 'pro'
    except Exception as er:
        print(er)
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':user,
    })
    
    
    
    