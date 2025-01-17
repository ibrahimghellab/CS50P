from jar import Jar

def test_init():
    jar=Jar(4)
    assert jar.capacity==4
    assert jar.size==0

def test_str():
    jar=Jar()
    assert str(jar)==""
    jar.deposit(5)
    assert str(jar)=="🍪🍪🍪🍪🍪"

def test_deposit():
    jar=Jar()
    jar.deposit(5)
    assert jar.size==5
    jar.deposit(5)
    assert jar.size==10
    jar.deposit(2)
    assert jar.size==12


def test_withdraw():
    jar=Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size==3
    jar.deposit(9)
    jar.withdraw(12)
    assert jar.size==0


