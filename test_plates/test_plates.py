from plates import is_valid

def test_default():
    assert is_valid("AAA222")==True

def test_with_only_letters():
    assert is_valid("TEST")
    assert is_valid("HELOOO")
def test_alphabetical_start():
    assert is_valid("50CS")==False
    assert is_valid("CS50")==True
    assert is_valid("AAA5")==True
    assert is_valid("A2")==False

def test_problems():
    assert is_valid("CS05")==False
    assert is_valid("CS50P")==False
    assert is_valid("PI3.14")==False
    assert is_valid("OUTATIME")==False
    assert is_valid("50CCS")==False
