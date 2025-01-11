from playwright.sync_api import expect, Page
from tests.utils.constants import BASE_URL

def test_check(page: Page):
    page.goto(BASE_URL)
    # page.locator('//form//button[2]').click()
    # print(page.get_by_text('Valid first name is required').is_visible)
    # page.reload()
    # print(page.get_by_text('Valid first name is required').is_visible)
    checkbox = page.get_by_role('checkbox')
    textarea = page.locator('#textarea')
    message = 'msg'
    checkbox.check()
    textarea.fill(message)
    expect(textarea).to_have_value(message)
