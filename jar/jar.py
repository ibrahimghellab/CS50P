class Jar:

    def __init__(self, capacity=12):

        if(int(capacity)>=0):
            self._capacity=capacity
            self._size=0
        else:
            raise ValueError
    def __str__(self):
        result=""
        for _ in range(self._size):
            result+="🍪"
        return result

    def deposit(self, n):
        if(self._size+n<=self._capacity):
            self._size+=n
        else:
            raise ValueError

    def withdraw(self, n):
        if(self._size-n>=0):
            self._size-=n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


