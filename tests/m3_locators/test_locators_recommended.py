from playwright.sync_api import Page, expect, BrowserType
from tests.utils.constants import BASE_URL

# to slow things down
def test_headless_and_slow_mo(browser_type: BrowserType):
    page = browser_type.launch(headless=False, slow_mo=2000).new_page()


def test_recommended_locators(page: Page):
    page.goto(BASE_URL)

    page.get_by_label('First name').fill('Steve')  # Get element by value of text

    page.get_by_role('button', name='Register').click()
    page.get_by_role('button', name='Register', exact=True).click() # Makes it case sensitive

    warning = page.get_by_text('Valid last name is required')
    expect(warning).to_be_visible

