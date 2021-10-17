# python
from __future__ import unicode_literals
from typing import Generator

# libs
import pytest
from fastapi.testclient import TestClient

# local
from main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c