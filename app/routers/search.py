from fastapi import APIRouter
from pydantic import BaseModel

# For testing
import json
router = APIRouter()

# Search model
class SearchQuery(BaseModel):
    query: str

# Routes
@router.post("/search")
async def search(search_query: SearchQuery):
    """
    Perform a search through the list of anime and try to match items with approximate names in it's titles

    Returns:
        JSON:
            titles: the titles of animes
    """

    # For testing, open file directly and load it
    f = open('app/parsed-anime-list-mini.json')
    data = json.load(f)

    # Keep track of titles that are possible
    anime_list = {"titles": []}

    # Cycle through list to find an include
    for idx, item in enumerate(data):
        if search_query.query.lower() in item['title'].lower():
            anime_list['titles'].append(item['title'])

    return anime_list
