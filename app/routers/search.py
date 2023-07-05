from fastapi import APIRouter
from pydantic import BaseModel


# For testing
import json
import random

router = APIRouter()

# Search model
class SearchQuery(BaseModel):
    query: str

# Routes
@router.post("/search")
async def search(search_query: SearchQuery):

    # For testing, return 5 random items
    f = open('app/parsed-anime-list-mini.json')
    data = json.load(f)

    anime_list = {"titles": []}

    anime_list['titles'].append(data[random.randint(0,100)]['title'])
    anime_list['titles'].append(data[random.randint(0,100)]['title'])
    anime_list['titles'].append(data[random.randint(0,100)]['title'])
    anime_list['titles'].append(data[random.randint(0,100)]['title'])
    anime_list['titles'].append(data[random.randint(0,100)]['title'])

    return anime_list
