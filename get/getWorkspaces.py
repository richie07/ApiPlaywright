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

def test_getRegres( api_request_context: APIRequestContext):
    response = api_request_context.get("")
    print(response.body())
    assert response.status == 200