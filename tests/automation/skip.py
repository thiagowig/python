import pytest


def setup():
    print("setup")

@pytest.mark.xfail
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.xfail
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.skip
def test_less():
   num = 100
   assert num < 200

def teardown():
    print("teardown")