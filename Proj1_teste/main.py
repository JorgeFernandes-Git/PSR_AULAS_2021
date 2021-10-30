#!/usr/bin/python3

import string
import random
import readchar
from colorama import Fore, Back, Style
from time import time, ctime
import argparse


def average(lst):
    return sum(lst) / len(lst)


def typing_test_max_val(max_value):
    # geração de letras
    typed_letter = ""
    cnt_letters = 0
    random_letter = ""
    num_letters_to_type = max_value
    # agrupar e contar letras lidas
    correct_letters = []
    wrong_letters = []
    cnt_correct_letters = 0
    cnt_wrong_letters = 0
    # contagem de tempo
    init_time = time()
    final_time = 0
    read_times = []
    avg_times = 0

    while True:
        if cnt_letters == num_letters_to_type:
            break
        else:
            cnt_letters += 1
            random_letter = random.choice(string.ascii_lowercase)
            print("Type the letter: " + random_letter)
            typed_letter = readchar.readkey()
            if typed_letter == random_letter:
                final_time = time() - init_time
                read_times.append(final_time)
                init_time = time()
                cnt_correct_letters += 1
                correct_letters.append(random_letter)
            else:
                final_time = time() - init_time
                read_times.append(final_time)
                init_time = time()
                cnt_wrong_letters += 1
                wrong_letters.append(random_letter)

    # contabilizar tempos
    avg_times = average(read_times)

    print("Current time: " + Fore.RED + Style.BRIGHT + ctime() + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + Back.YELLOW + "accuracy: " + str(avg_times) + " seconds" + Style.RESET_ALL)
    print("You typed " + Fore.RED + str(cnt_correct_letters) + Style.RESET_ALL + " correct letters")
    print(", ".join(correct_letters))
    print("You typed " + Fore.RED + str(cnt_wrong_letters) + Style.RESET_ALL + " incorrect letters")
    print(", ".join(wrong_letters))
    print("Time per typed letter:")
    print(read_times)


def typing_test_max_time(max_value):
    # geração de letras
    typed_letter = ""
    cnt_letters = 0
    random_letter = ""
    max_time_to_type = max_value
    # agrupar e contar letras lidas
    correct_letters = []
    wrong_letters = []
    cnt_correct_letters = 0
    cnt_wrong_letters = 0
    # contagem de tempo
    init_time = time()
    interm_tot_time = time()
    cnt_time = 0
    interm_time = 0
    read_times = []
    avg_times = 0

    while True:
        if cnt_time >= max_time_to_type:
            break
        else:
            cnt_time = time() - init_time
            random_letter = random.choice(string.ascii_lowercase)
            print("Type the letter: " + random_letter)
            typed_letter = readchar.readkey()
            if typed_letter == random_letter:
                interm_time = time() - interm_tot_time
                read_times.append(interm_time)
                interm_tot_time = time()
                cnt_correct_letters += 1
                correct_letters.append(random_letter)
            else:
                interm_time = time() - interm_tot_time
                read_times.append(interm_time)
                interm_tot_time = time()
                cnt_wrong_letters += 1
                wrong_letters.append(random_letter)

    # contabilizar tempos
    avg_times = average(read_times)

    print("Current time: " + Fore.RED + Style.BRIGHT + ctime() + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + Back.YELLOW + "accuracy: " + str(avg_times) + " seconds" + Style.RESET_ALL)
    print("You typed " + Fore.RED + str(cnt_correct_letters) + Style.RESET_ALL + " correct letters")
    print(", ".join(correct_letters))
    print("You typed " + Fore.RED + str(cnt_wrong_letters) + Style.RESET_ALL + " incorrect letters")
    print(", ".join(wrong_letters))
    print("Time per typed letter:")
    print(read_times)


def main():
    parser = argparse.ArgumentParser(description="Definition of test mode")
    parser.add_argument("-utm", "--use_time_mode", action="store_true", help="Max number of secs for time mode or "
                                                                             "maximum number of inputs for number of"
                                                                             " inputs mode.")
    parser.add_argument("-mv", "--max_value", type=int, help="Max number of secs for time mode or maximum number of "
                                                             "inputs for number of inputs mode.")
    args = vars(parser.parse_args())
    print(args)

    if args["use_time_mode"]:
        print("Using time mode. Test will run for " + str(args["max_value"]) + " seconds")
        typing_test_max_time(args["max_value"])
    else:
        print("Not using time mode. Test will ask for " + str(args["max_value"]) + " responses")
        typing_test_max_val(args["max_value"])


if __name__ == '__main__':
    main()
