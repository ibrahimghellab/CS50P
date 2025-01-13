from numb3rs import validate
def test_default():
    assert validate("127.0.0.1")==True

def test_max():
    assert validate("255.255.255.255")==True

def test_more():
    assert validate("512.512.512.512")==False

def test_one_more():
    assert validate("11.2.3.1000")==False

def test_alphabetical():
    assert validate("cat")==False

def test_only_one():
    assert validate("1.256.256.256")==False
