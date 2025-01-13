from playwright.sync_api import expect, Page, Browser
from tests.utils.constants import BASE_URL

def disable_js(browser: Browser):
    browser.new_context(java_script_enabled=False)

def test_route_abort(page: Page):
    # page.route('**/*.{js,png}') # Blocks all .js and .png files
    page.route('**/*.{js}', lambda route: route.abort()) # Block all .js files and abort
    page.goto(f'{BASE_URL}savings.html')
    page.get_by_test_id('deposit').fill('10')
    expect(page.get_by_test_id('result')).not_to_be_visible()


def test_route_with_condition(page: Page):
    page.route('**/*', lambda route: route.abort() 
    if route.request.resoure_type == 'script' else route.continue_())
    # Your test code here
    # page.goto(...) and other actions


def test_route_fulfill(page: Page):
    page.route('**/*.pdf', lambda route: route.fulfill(
        status=404,
        content_type='text/plain',
        body='Not found'
    ))
    page.goto(f'{BASE_URL}savings.html')
    page.get_by_text('Download Our Offer').click()
    page.screenshot(path='route.png')
    page.wait_for_url('**/*.pdf')
    body = page.locator('body')
    expect(body).to_contain_text('Not found')
