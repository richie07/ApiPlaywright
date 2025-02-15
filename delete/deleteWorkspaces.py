from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/json",
        "X-API-Key": "PMAK-XXXXX"
    }
    request_context = playwright.request.new_context(
        base_url="https://api.getpostman.com/environments/", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()

def test_putRegres( api_request_context: APIRequestContext):
    body = {
        "environment": {
            "name": "Environment Test1"
        }
    }
    response = api_request_context.post("",data = body)
    #print(response.body())
    assert response.status == 200
    id = response.json()["environment"]["id"]

    response1 = api_request_context.delete(id)
    #print(response.body())
    assert response1.status == 200
    assert response1.json()["environment"]["id"] == id

    response2 = api_request_context.delete(id)
    # print(response.body())
    assert response2.status == 404
    assert response2.json()["error"]["name"] == "instanceNotFoundError"
    assert response2.json()["error"]["message"] == "The specified environment does not exist."
