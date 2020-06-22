import math
import pytest

@pytest.mark.great
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5