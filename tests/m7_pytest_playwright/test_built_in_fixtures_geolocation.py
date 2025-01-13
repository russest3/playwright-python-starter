import pprint
from time import sleep
from playwright.sync_api import Playwright
from pprint import pprint


def test_geolocation(playwright: Playwright):
    ipad: dict = playwright.devices['iPad Pro 11']
    pprint(playwright.devices)

    ctx = playwright.chromium.launch(headless=False, slow_mo=1000).new_context(
        # **ipad,         # Expands the dictionary
        user_agent='Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) '
                   'AppleWebKit/605.1.15 (KHTML, Like Gecko) '
                   'Version/18.0 Mobile/15E148 Safari/604.1',
        locale='en_GB',
        geolocation={"longitude": 135.580371396737874, "latitude": -78.84049039068572},
        permissions=["geolocation"],
        base_url='https://maps.google.com/'
    )
    
    page = ctx.new_page()
    page.goto('')
    page.get_by_role('button', name='Accept all').click()
    page.get_by_role('button', name='Stay on web').click()
    sleep(2)
