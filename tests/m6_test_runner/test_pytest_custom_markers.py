import pytest
import sys

# @pytest.mark.skip(reason='...') # Mark a reason to skip a test
# @pytest.mark.skipif(sys.platform =='win32', reason='...')  # Mark a reason to skip if
def test_smoke():
    assert 2 == 2
