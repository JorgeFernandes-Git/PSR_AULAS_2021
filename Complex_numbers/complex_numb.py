#!/usr/bin/python3

def addComplex(x, y):
    # add code here ...
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    return (a + c, b + d)


def multiplyComplex(x, y):
    # add code here ...
    pass
def printComplex(x):
    # add code here ...
    pass

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()