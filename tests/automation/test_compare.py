import pytest



def test_greater(input_value):
   num = 100
   assert num > 100

@pytest.mark.integration_test
def test_greater_equal():
   num = 100
   assert num >= 100

def test_less():
   num = 100
   assert num < 200