from time import sleep
import pytest
from playwright.sync_api import Page, Browser, Playwright
from tests.utils.constants import BASE_URL


def test_page_fixture(page: Page):
    name_input = page.get_by_label('First name')


# Playwright > BrowserType > Browser > Context (virtual container) > Page (single browser tab)
def test_different_browsers(playwright: Playwright):
    # If you need to test multiple browsers you cannot use Page use this instead:
    chromium_page = playwright.chromium.launch().new_context().new_page()
    firefox_page = playwright.firefox.launch().new_context().new_page()
    


def test_browser(browser: Browser):
    ctx = browser.new_context(
        viewport={'width': 400, 'height': 200},
        locale='es_ES',
        base_url='https://google.com/'
    )  # defaults to Chromium if no browser specified
    page = ctx.new_page()
    page.goto('')
    sleep(2)
    page.screenshot(path='result.png')


def test_browser_type(is_chromium):
    if is_chromium:
        print('...')
        pytest.skip('Reason...')


def test_incomplete_fixture_name(playwright: Playwright, page: Page):
    page.goto(BASE_URL)
    new_page = playwright.chromium.launch().new_page()



