from operator import ne
from re import I


def mygen():
    for i in range(1, 1000):
        result = i * I
        yield result


# gen = (i * i for i in range(1, 1000))

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))


class MyIterator:
    def __init__(self):
        self.data = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.data * self.data
        self.data += 1
        if self.data >= 1000:
            raise StopIteration
        return result
