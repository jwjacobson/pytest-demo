from main import add, subtract, divide

import pytest

def test_add_positive_integers():
    result = add(1, 2)
    expected = 3
    
    assert result == expected

def test_add_negative_integers():
    result = add(-4, -9)
    expected = -13

    assert result == expected


def test_subtract():
    result = subtract(3, 1)
    expected = 2

    assert result == expected

def test_divide():
    result = divide(10, 2)

    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = divide(1, 0)