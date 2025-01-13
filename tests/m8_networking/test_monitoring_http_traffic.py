from playwright.sync_api import expect, Page
from tests.utils.constants import BASE_URL

# def test_monitoring_http_traffic(page: Page):
#     page.on('request', lambda request: print(f'>> {request.method} {request.url}'))
#     page.on('response', lambda response: print(f'<< {response.status} {response.url}'))

#     page.goto(BASE_URL)

# Assert that all response status code is less than 400
console_messages = []
def test_http_traffic(page: Page):
    page.on('response', lambda response: console_messages.append(response) if response.status >=400 else None)
    page.goto(BASE_URL)
    assert len(console_messages) == 0, 'Expected 0 errors'
    
