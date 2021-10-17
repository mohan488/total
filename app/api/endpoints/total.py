# python
from __future__ import unicode_literals
from typing import Dict, List

# libs
from fastapi import APIRouter
from starlette.status import HTTP_200_OK

# local
from app.schemas.total import Total


router = APIRouter()


@router.get("/", response_model=Total, status_code=HTTP_200_OK)
async def total() -> Dict:

    """
    Sum of a list of numbers
    ---
    tags:
        - Total

    get:

        parameters:
            - N/A

        response:
            200:
                description: returns a dictionary with a total sum of a list of numbers

    """
    
    return {"total": sum(list(range(10000001)))}
