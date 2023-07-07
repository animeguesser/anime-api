from fastapi import APIRouter
from pydantic import BaseModel

# For testing
import json
router = APIRouter()

# Search model
class AnswerQuery(BaseModel):
    answer: str

# Routes
@router.post("/answer")
async def search(answer_query: AnswerQuery):
    """
    Validate that the answer is correct or incorrect

    Returns:
        JSON:
            answer: {true | false}
    """

    # Hard coded answer for testing
    if answer_query.answer.lower() == "Cowboy Bebop".lower():
        return {'answer':True}
    else:
        return {'answer':False}
