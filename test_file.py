
import pytest

import taller

def test_getCost():
    order = {"Hamburger": 2, "Salad": 1}
    expected_result = 14
    result = taller.getCost(order)
    assert result == expected_result

#Test the function applyDiscount
def test_applyDiscount():
    #Create a variable with the expected result
    expected_result = 42.2
    #Call the function to test
    result = taller.applyDiscount(52.2)
    #Compare the result with the expected result
    assert result == expected_result
