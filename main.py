#import pytest
from utils import calculate_ch

def test_calculate_ch():
    price = "4000"
    cash = "5000"
    result = calculate_ch(price, cash)
    assert result == "1000 - 1.0 шт."

def test_calculate_ch():
    price = "8345"
    cash = "5000 5000"
    result = calculate_ch(price, cash)
    assert result == "1000 - 1.0 шт., 500 - 1.0 шт.," \
                     "100 - 1.0 шт., 50 - 1.0 шт., 5 - 1.0 шт. "

def test_calculate_ch():
    price = "151.10"
    cash = "100 50 5"
    result = calculate_ch(price, cash)
    assert result == "2 - 1.0 шт., 1 - 1.0 шт., 0.5 - 1.0 шт., 0.1 - 4.0 шт."

def test_calculate_ch():
    price = "565"
    cash = "1000"
 #   with pytest.raises(ValueError):
 #       calculate_ch(price, cash)

def test_calculate_ch():
    price = "900"
    cash = "500 0,1"
    result = calculate_ch(price, cash)
    assert result == "Недостаточно внесенных средств"
