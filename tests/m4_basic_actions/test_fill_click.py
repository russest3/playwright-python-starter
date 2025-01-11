from playwright.sync_api import Page
from tests.utils.constants import BASE_URL


def test_fill(page: Page):
    page.goto(BASE_URL)
    page.get_by_label('First name').fill('Steve')
    page.get_by_label('Date of birth').fill('2024-10-28') # Format must be in Year-Month-Date!


def test_click_demo(page: Page):
    page.goto(BASE_URL)
    btn = page.get_by_role('button', name='Register')
    btn.click(click_count=5)
    btn.dblclick()
    btn.click(button='right')
