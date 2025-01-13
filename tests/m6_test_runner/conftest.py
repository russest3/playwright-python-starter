import pytest

@pytest.fixture(scope='session', autouse=True) # Now runs once before all tests
def global_setup_available_everywhere():
    print('Global setup for entire test run of ALL applicable tests')