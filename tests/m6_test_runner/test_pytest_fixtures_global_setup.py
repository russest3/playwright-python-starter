from typing import Any
import pytest
from playwright.sync_api import expect, Page
from tests.utils.constants import BASE_URL
import requests

@pytest.fixture(scope='module') #scope causes it to only run once
def once_per_module():
    # For slow queries to a database use requests instead
    print('Run once for all tests')
    name = requests.get('https://api.github.com/users/andrejs-ps').json().get('name')
    yield name

@pytest.fixture
def page(page: Page):
    page.goto(BASE_URL)
    yield page
    # do cleanup


def test_one(page: Page, once_per_module: Any):
    name_input = page.get_by_label('First name')
    name_input.fill('')
    expect(name_input).to_have_value('')

    print(f'Test 1: ${once_per_module}')


def test_two(page: Page, once_per_module: Any):
    name_input = page.get_by_label('First name')
    name_input.fill('')
    expect(name_input).to_have_value('')

    print(f'Test 2: ${once_per_module}')
