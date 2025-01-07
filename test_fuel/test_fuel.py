from fuel import convert
from fuel import gauge
import pytest

def test_default():
    assert convert("3/4")==75
    assert gauge(75)=="75%"
    assert convert("1/4")==25
    assert gauge(25)=="25%"

def test_full():
    assert convert("4/4")==100
    assert gauge(100)=="F"
    assert gauge(99)=="F"
def test_empty():
    assert convert("0/4")==0
    assert gauge(0)=="E"
    assert gauge(1)=="E"

def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/hello")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
