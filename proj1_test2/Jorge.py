#!/usr/bin/python3

import string
import random
import readchar
from colorama import Fore, Back, Style
from time import time, ctime
import argparse
from collections import namedtuple
import pprint

Input = namedtuple("Input", ["requested", "received", "duration"])
my_dict = {
    "accuracy": 0.0,
    "inputs": [Input(requested="", received="", duration=0.0)],
    "number_of_hits": 0,
    "number_of_types": 0,
    "test_duration": 0.0,
    "test_end": "",
    "test_start": "",
    "type_average_duration": 0.0,
    "type_hit_average_duration": 0.0,
    "type_miss_average_duration": 0.0
}

# geração de letras
typed_letter = ""
cnt_letters = 0
random_letter = ""

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
read_correct_times = []
read_incorrect_times = []
avg_times = 0.0
avg_correct_times = 0.0
avg_incorrect_times = 0.0

inputs_list = []


def average(lst):
    if len(lst) != 0:
        return sum(lst) / len(lst)
    else:
        return 0


def print_my_dict():
    my_dict["accuracy"] = (cnt_correct_letters / (cnt_correct_letters + cnt_wrong_letters)) * 100
    my_dict["inputs"] = inputs_list
    my_dict["number_of_hits"] = cnt_correct_letters
    my_dict["number_of_types"] = cnt_correct_letters + cnt_wrong_letters
    my_dict["test_duration"] = cnt_time
    my_dict["test_end"] = ctime()
    my_dict["test_start"] = ctime()
    my_dict["type_average_duration"] = avg_times
    my_dict["type_hit_average_duration"] = avg_correct_times
    my_dict["type_miss_average_duration"] = avg_incorrect_times

    print(Fore.GREEN + "Test completed. Results:" + Style.RESET_ALL)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(my_dict)


def typing_test_max_val(max_value):
    num_letters_to_type = max_value
    global cnt_letters
    global cnt_correct_letters
    global cnt_wrong_letters
    global interm_time
    global interm_tot_time
    global avg_times
    global avg_correct_times
    global avg_incorrect_times
    global cnt_time
    global random_letter
    global typed_letter
    global inputs_list

    while True:
        if cnt_letters == num_letters_to_type:
            break
        else:
            cnt_letters += 1
            random_letter = random.choice(string.ascii_lowercase)
            print("Type the letter: " + Fore.GREEN + random_letter + Style.RESET_ALL)
            typed_letter = readchar.readkey()
            if typed_letter == random_letter:
                interm_time = time() - interm_tot_time
                read_times.append(interm_time)
                read_correct_times.append(interm_time)
                interm_tot_time = time()
                cnt_correct_letters += 1
                correct_letters.append(random_letter)
            else:
                interm_time = time() - interm_tot_time
                read_times.append(interm_time)
                read_incorrect_times.append(interm_time)
                interm_tot_time = time()
                cnt_wrong_letters += 1
                wrong_letters.append(random_letter)
            print("You typed the letter " + Fore.BLUE + typed_letter + Style.RESET_ALL)
            inputs_list.append(Input(requested=random_letter, received=typed_letter, duration=interm_time))

    # contabilizar tempos
    avg_times = average(read_times)
    cnt_time = time() - init_time
    avg_correct_times = average(read_correct_times)
    avg_incorrect_times = average(read_incorrect_times)

    print_my_dict()


def typing_test_max_time(max_value):
    max_time_to_type = max_value
    global cnt_letters
    global cnt_correct_letters
    global cnt_wrong_letters
    global interm_time
    global interm_tot_time
    global avg_times
    global avg_correct_times
    global avg_incorrect_times
    global cnt_time
    global random_letter
    global typed_letter
    global inputs_list

    while True:
        if cnt_time >= max_time_to_type:
            break
        else:
            cnt_time = time() - init_time
            random_letter = random.choice(string.ascii_lowercase)
            print("Type the letter: " + Fore.GREEN + random_letter + Style.RESET_ALL)
            typed_letter = readchar.readkey()
            if typed_letter == random_letter:
                interm_time = time() - interm_tot_time
                read_times.append(interm_time)
                read_correct_times.append(interm_time)
                interm_tot_time = time()
                cnt_correct_letters += 1
                correct_letters.append(random_letter)
            else:
                interm_time = time() - interm_tot_time
                read_times.append(interm_time)
                read_incorrect_times.append(interm_time)
                interm_tot_time = time()
                cnt_wrong_letters += 1
                wrong_letters.append(random_letter)
            print("You typed the letter " + Fore.BLUE + typed_letter + Style.RESET_ALL)
            inputs_list.append(Input(requested=random_letter, received=typed_letter, duration=interm_time))

    # contabilizar tempos
    avg_times = average(read_times)
    avg_correct_times = average(read_correct_times)
    avg_incorrect_times = average(read_incorrect_times)

    print_my_dict()


def main():
    parser = argparse.ArgumentParser(description="Definition of test mode")
    parser.add_argument("-utm", "--use_time_mode", action="store_true", help="Max number of secs for time mode or "
                                                                             "maximum number of inputs for number of"
                                                                             " inputs mode.")
    parser.add_argument("-mv", "--max_value", type=int, help="Max number of secs for time mode or maximum number of "
                                                             "inputs for number of inputs mode.")
    args = vars(parser.parse_args())
    print(args)
    print("PSR 2021 Typing test")

    if args["use_time_mode"]:
        print("Test running up to " + str(args["max_value"]) + " seconds.")
        print("Press any key to start...")
        pressed_continue = readchar.readkey()
        typing_test_max_time(args["max_value"])
    else:
        print("Test running up to " + str(args["max_value"]) + " inputs.")
        print("Press any key to start...")
        pressed_continue = readchar.readkey()
        typing_test_max_val(args["max_value"])


if __name__ == '__main__':
    main()
