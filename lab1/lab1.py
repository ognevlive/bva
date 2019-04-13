from math import *
from sys import argv


def f(x):
    return (x + ceil(abs(tan(degrees(x))))*ceil(log2(x))) % 2**32


# a = 2
# for i in range(5):
#     a = f(a)
#     print(a)


def floyd(start):
    a = start
    b = f(a)

    print("a = %d" % a)
    print("b = %d" % b)

    while a != b:
        a = f(a)
        b = f(f(b))

    b = [f(a)]

    t = 1

    while a != b[t-1]:
        b.append(f(b[t-1]))
        t = t + 1

    print(a)
    print(b[-1])
    print(t)


def gosper():
    
    pass


if __name__ == '__main__':
    if len(argv) < 2:
        print('not enough arguments')
    elif argv[1] == 'floyd':
        floyd(2)
    elif argv[1] == 'gosper':
        gosper()
