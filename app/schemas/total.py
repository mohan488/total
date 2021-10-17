# python
from __future__ import unicode_literals

# libs
from pydantic import BaseModel

# local


#Properties to return via API
class Total(BaseModel):
    total: int