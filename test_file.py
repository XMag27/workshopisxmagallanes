
import pytest

import taller

def test_getCost():
    order = {"Hamburger": 2, "Salad": 1}
    expected_result = 14
    result = taller.getCost(order)
    assert result == expected_result

#Test the function applyDiscount
def test_applyDiscount():
    expected_result = 42.2
    result = taller.applyDiscount(52.2)
    assert result == expected_result

def test_applyDiscount2():
    expected_result = 85.0
    result = taller.applyDiscount(110)
    assert result == expected_result

def test_getCost2():
    order = {"Hamburger": 20, "Salad": 1}
    expected_result = 104.0
    result = taller.getCost(order)
    assert result == expected_result