from playwright.sync_api import Page, expect

expect.set_options(timeout=10_000)

def test_homepage_title(page: Page):
    page.goto('http://localhost:8000/')   # Run previous code with all defaults
    expect(page).to_have_title('Credit Association')
    expect(page).to_have_url('http://localhost:8000/')

def test_homepage_header(page: Page):
    page.goto('http://localhost:8000/')    # Run previous code with all defaults
    header = page.get_by_text('Register to become a member')
    expect(header).to_be_visible()

def test_homepage_copyright(page: Page):
    page.goto('http://localhost:8000/')    # Run previous code with all defaults
    locator = page.locator("xpath=//*[@id='copyright']")
    expect(locator).to_contain_text('© 2025')
