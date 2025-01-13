from typing import Any
import pytest
from playwright.sync_api import expect, Page, Playwright, APIResponse, APIRequestContext, Response
from tests.utils.constants import BASE_URL
import requests



@pytest.fixture(scope='module') # module scope causes it to only run once
def once_per_module(playwright: Playwright, page: Page):
    # For slow queries to a database use requests instead
    # This code rewritten using playwright below
    # print('Run once for all tests')
    # name = requests.get('https://api.github.com/users/andrejs-ps').json().get('name')
    # yield name

    response: Response = page.goto(BASE_URL)
    api_ctx: APIRequestContext = page.request
    api_response: APIResponse = api_ctx.get(BASE_URL)
    print('Run once for all tests')
    independent_api_ctx = playwright.request.new_context()
    _response = independent_api_ctx.get(BASE_URL)
    _response
    yield name

# @pytest.fixture
# def page(page: Page):
#     page.goto(BASE_URL)
#     yield page
#     do cleanup


def test_one(page: Page, once_per_module: Any):
    name_input = page.get_by_label('First name')
    name_input.fill('')
    expect(name_input).to_have_value('')

    print(f'Test 1: ${once_per_module}')


# def test_two(page: Page, once_per_module: Any):
#     name_input = page.get_by_label('First name')
#     name_input.fill('')
#     expect(name_input).to_have_value('')

#     print(f'Test 2: ${once_per_module}')
