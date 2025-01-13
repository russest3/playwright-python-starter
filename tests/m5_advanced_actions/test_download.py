from tests.utils.constants import BASE_URL
from playwright.sync_api import Page, sync_playwright, Playwright

def test_download(playwright: Playwright):
    # page = playwright.chromium.launch(headless=False, slow_mo=1000).new_page()
    page = playwright.chromium.launch(headless=True, slow_mo=1000).new_page() # For PDFs run in headless mode
    page.goto(f'{BASE_URL}savings.html')

    with page.expect_download() as download_info:
        page.get_by_role('button', name='Download Our Offer').click()
    
    download = download_info.value
    print(download)
    print(download.suggested_filename)

    assert download.suggested_filename == 'dummy.pdf'
    download.save_as(download.suggested_filename)