# python
from __future__ import unicode_literals

# libs
from fastapi import APIRouter

# local
from app.api.endpoints import total

api_router = APIRouter()
api_router.include_router(total.router, prefix="/total", tags=["total"])