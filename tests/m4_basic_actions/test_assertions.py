from playwright.sync_api import expect, Page
from tests.utils.constants import BASE_URL

def assertions_cheatsheet(page: Page):
    page.goto(BASE_URL)
    textarea = page.locator('#textarea')
    expect(textarea).to_have_value('...')  # text inputs and text areas

    expect(page.locator('h4')).to_contain_text('...') # text contains
    expect(page.locator('h4')).to_have_text('...') # text is exactly
    
