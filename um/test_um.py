from um import count

def test_default():
    assert count("hello, um, world")==1

def test_brain():
    assert count("instrumentation")==0

def test_with_space_around():
    assert count(" um ")==1

def test_with_insensitive_case():
    assert count("UM")==1
