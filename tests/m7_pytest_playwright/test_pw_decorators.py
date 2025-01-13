import pytest
from playwright.sync_api import Page, Browser


# You could also move this dict to a util file and import it instead
args: dict = {"locale": 'es_ES', "timezone_id": "Europe/Madrid"}

class TestThing:

    @pytest.mark.skip_browser('firefox') # Skip firefox test for this one
    def test_one(self, page: Page):
        pass

    @pytest.mark.only_browser('firefox')
    def test_two(self, page: Page):
        pass
    
    @pytest.mark.browser_context_args(**args) # ** Expands the dictionary object
    def test_three(self, page: Page, browser: Browser):
        browser.new_context(**args)
        assert page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone") == "Europe/Madrid"
        assert page.evaluate("window.navigator.languages") == ["es-ES"]


    @pytest.mark.parametrize('arg1', ['val1',
                                      'val2'])
    @pytest.mark.browser_context_args(**args)
    @pytest.mark.smoke
    def test_four(self, page: Page, arg1: str):
        assert page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone") == "Europe/Madrid"
        assert page.evaluate("window.navigator.languages") == ["es-ES"]
