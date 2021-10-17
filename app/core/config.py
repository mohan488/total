# python
from __future__ import unicode_literals
from typing import List, Union

# libs
from pydantic import AnyHttpUrl, BaseSettings, validator, Field

# local


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4658", "http://localhost:3000", \
    # "http://localhost:8080"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "Total"
    VERSION: str = "0.0.1"
    DESCRIPTION: str = "Project micro-service is used to get the sum of a \
        list of numbers, the service processes all the requests \
            asynchronously. written in Python/FastAPI"

    
    class Config:
        case_sensitive = True


settings = Settings()