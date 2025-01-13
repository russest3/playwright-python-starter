from pprint import pprint
from tests.utils.constants import BASE_URL

from playwright.sync_api import expect, Page

name = 'Sofia'


def test_storage_ui_perspective(page: Page):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)
    page.reload()
    expect(name_input).to_have_value('')

    name_input.fill(name)
    page.get_by_role('button', name='Save Input').click()
    page.reload()
    expect(name_input).to_have_value(name)


def test_local_storage(page: Page):
    page.goto(BASE_URL)
    page.get_by_label('First name').fill(name)
    page.get_by_role('button', name='Save Input').click()

    StorageState = page.context.storage_state()

    print(StorageState)
    print(StorageState['cookies'])
    print(StorageState['origins'][0]['localStorage'])

def test_javascript_and_storage(page: Page):
    page.goto(BASE_URL)
    name_input = page.get_by_label('First name')
    name_input.fill(name)
    page.get_by_role('button', name='Save Input').click()
    print('')
    storage: dict = page.evaluate('() => window.localStorage') #Evaluates Javascript on page
    print(storage)
    page.evaluate('() => window.localStorage.clear()')
    page.reload()
    expect(name_input).to_have_value('')
    page.evaluate('() => window.localStorage.setItem("firstName", "Steve")')
    page.reload()
    expect(name_input).to_have_value('Steve')

def test_session_storage(page: Page):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)
    page.get_by_role('button', name='Save Input').click()
