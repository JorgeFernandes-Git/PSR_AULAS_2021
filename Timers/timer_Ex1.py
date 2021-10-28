#!/usr/bin/python3

import math
from colorama import Fore, Back, Style
from time import time, ctime


def RootCalc(init_num, final_num):
    square_root = 0
    roots_to_print = []
    for i in range(init_num, final_num + 1):
        square_root = math.sqrt(i)
        # print(square_root)
        if square_root > 100:
            roots_to_print.append(square_root)

    # print(roots_to_print)


def main():

    init_num = 0
    final_num = 5000000

    init_time = time()
    final_time = 0

    RootCalc(init_num, final_num)

    print("This is the current time: " + Fore.RED + Style.BRIGHT + Back.YELLOW + ctime() + Style.RESET_ALL)

    # print(time())
    # print(ctime())

    final_time = time() - init_time

    print("Time spent to calculate the square roots from " + str(init_num) + " until " + str(final_num) + ":")
    print(str(final_time) + " seconds")


if __name__ == '__main__':
    main()
