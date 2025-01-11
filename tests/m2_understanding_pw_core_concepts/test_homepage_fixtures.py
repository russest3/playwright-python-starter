from playwright.sync_api import Page, expect

def test_homepage_title(page: Page):
    page.goto('http://localhost:8000/')   # Run previous code with all defaults

def test_homepage_header(page: Page):
    page.goto('http://localhost:8000/')    # Run previous code with all defaults
    header = page.locator('h4')
    assert header.text_content() == 'Register to become a member'

def test_homepage_copyright(page: Page):
    page.goto('http://localhost:8000/')    # Run previous code with all defaults
    header = page.get_by_test_id('copyright')
    # assert copyright.text_content() == '© 2025'
    expect(copyright).
