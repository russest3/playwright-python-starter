from playwright.sync_api import expect, Page
from tests.utils.constants import BASE_URL

home_title = 'Credit Association'
savings_title = 'Save with us'


def test_back_forward_reload(page: Page):
    page.goto(BASE_URL)
    page.goto(f'{BASE_URL}savings.html')
    expect(page).to_have_title(savings_title)
    page.go_back()
    expect(page).to_have_title(home_title)
    page.go_forward()
    expect(page).to_have_title(savings_title)
    page.reload()
    expect(page).to_have_title(savings_title)


def test_navigation(page: Page):
    page.goto(f'{BASE_URL}savings.html'), wait_until='load', timeout=100)
    expect(page).to_have_title(home_title)


def test_load_speed_while_navigating(page: Page):
    page.goto(BASE_URL, timeout=3000)
    page.goto(f'savings.html', timeout=3000)
    expect(page).to_have_title(savings_title)
