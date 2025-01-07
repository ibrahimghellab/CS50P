from bank import value

def test_default():
    assert value("hello")==0
    assert value("hey")==20
    assert value("what's up")==100

def test_with_capitalize_letters():
    assert value("hello".upper())==0
    assert value("hey".upper())==20
    assert value("what's up".upper())==100

def test_with_number():
    assert value("hello99")==0
    assert value("hey4247544")==20
    assert value("wh6546486at's up4564")==100

def test_with_punctuation():
    assert value("hello!")==0
    assert value("hey!")==20
    assert value("what's up!")==100

