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
    result = requests.get(url)
    if result.status_code != 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    result = result.json()
    
    user = {
        'name' : github_name,
    }
    try:
        user['public_repos'] = result['public_repos'] 
    except Exception as er:
        print(er)
    try:
        user['pro'] = result['plan']['name'] == 'pro'
    except Exception as er:
        print(er)
        
    url = f'https://api.github.com/users/{github_name}/repos'
    result = requests.get(url)
    if result.status_code != 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    result = result.json()
    
    repos = list()
    try:
        for i in result:
            repos.append({
                'name':i['name'],
                'language': i['language'],
                'created_at': i['created_at'],
            })
    except Exception as er:
        print(er)
    user['repos'] = repos
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        'details':user,
    })
    
    
    
    