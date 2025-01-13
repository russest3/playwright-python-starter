from pprint import pprint
from tests.utils.constants import BASE_URL
from playwright.sync_api import expect, Browser, Page, APIResponse, Playwright, APIRequestContext, Response


def test_api_request_response(page: Page, browser: Browser):
    # browser.new_context().request  # would work but best to avoid the browser

    response: Response = page.goto(BASE_URL)
    api_ctx: APIRequestContext = page.request

    # Now you have acccess to a number of http methods:
    # api_ctx.delete()
    # api_ctx.post()
    # api_ctx.put() # And so forth...

    api_response: APIResponse = api_ctx.get('https://api.github.com/')

    print(api_response.ok)
    print(api_response.status)
    pprint(api_response.headers_array())
    pprint(api_response.json())

    expect(api_response).to_be_ok()
    expect(response).to_be_ok() # THIS FAILS, MUST USE API_RESPONSE!


def test_api_request_context(playwright: Playwright):
    independent_api_ctx = playwright.request.new_context(base_url='...')
    independent_api_ctx.get('') #...