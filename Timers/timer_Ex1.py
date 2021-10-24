#!/usr/bin/python3
import math
from time import time, ctime

def main():

    square_root = 0
    init_num = 0
    final_num = 50000

    for i in range(init_num, final_num + 1):
        square_root = math.sqrt(i)
        print(square_root)

if __name__ == '__main__':
    main()

