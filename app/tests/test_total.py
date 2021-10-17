# python
from __future__ import unicode_literals

# libs
from fastapi.testclient import TestClient

# local


def test_get_total(client: TestClient) -> None:
    
    response = client.get(
        "api/v1/total/"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["total"] == 50000005000000