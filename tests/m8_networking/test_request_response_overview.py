from playwright.sync_api import Page, Response, Request
from tests.utils.constants import BASE_URL
from pprint import pprint


def test_request_response_overview(page: Page):
    response: Response = page.goto(BASE_URL)

    print(response.url)
    print(response.status)
    print(response.ok) # True if status code is 200-299

    pprint(response.all_headers()) # Returns a Dict[str, str]
    pprint(response.headers_array()) # Returns List[NameValue]

    print(response.body()) # Returns bytes, but still readable
    print(response.text()) # Returns str object

    request: Request = response.request
    print(request.all_headers())
    print(request.method)

