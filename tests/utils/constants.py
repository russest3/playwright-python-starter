from playwright.sync_api import Page, BrowserType

BASE_URL = 'http://localhost:8000/'

def test_headless_and_slow_mo(browser_type: BrowserType):
    page = browser_type.launch(headless=False, slow_mo=2000)
    # page = browser_type.launch(headless=False, slow_mo=2000).new_page()

def test_recommended_locators(page: Page):
    page.goto(BASE_URL)

