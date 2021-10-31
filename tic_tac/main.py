#!/usr/bin/python3

import time


def tic():
    seconds = time.time()
    tempo_atual = time.localtime(seconds)
    tempo_segundos = time.mktime(tempo_atual)
    return tempo_segundos


def tac():
    seconds = time.time()
    tempo_atual = time.localtime(seconds)
    tempo_segundos = time.mktime(tempo_atual)
    return tempo_segundos


def main():
    seconds = time.time()
    print(seconds)
    # tempo_atual = time.localtime(seconds)
    # print(tempo_atual)
    # tempo_segundos = time.mktime(tempo_atual)
    # print(tempo_segundos)


    # x = tac()
    # print(x)
    # time.sleep(0.51)
    # y = tac()
    # print(y)
    #
    # c = y - x
    # print(c)


if __name__ == '__main__':
    main()
