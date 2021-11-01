#!/usr/bin/python3

import string
import random
import readchar
from colorama import Fore, Style, Back
from time import time, ctime
import argparse
from collections import namedtuple
import pprint

Input = namedtuple("Input", ["requested", "received", "duration"])  # tuplo de inputs

# dicionário de resultados
Statistics = {
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
typed_letter = ""           # letra inserida pelo utilizador
cnt_letters = 0             # contador de letras inseridas
random_letter = ""          # letra gerada pelo programa aleatóriamente

# agrupar e contar letras lidas
correct_letters = []        # letras inseridas corretas
wrong_letters = []          # letras inseridas incorretas
cnt_correct_letters = 0     # contador de letras corretas
cnt_incorrect_letters = 0       # contador de letras incorretas

# contagem de tempo
init_time = 0               # tempo de início do modo
interm_tot_time = 0         # tempo de início
cnt_time = 0                # conta o tempo decorrido no ciclo
interm_time = 0             # conta os tempos intermédios entre cada letra
read_times = []             # lista para guardar os tempos de cada letra inserida
read_correct_times = []     # lista para guardar os tempos de cada letra inserida correta (hit)
read_incorrect_times = []   # lista para guardar os tempos de cada letra inserida incorreta (miss)
avg_times = 0.0             # média de tempos
avg_correct_times = 0.0     # média de tempos corretos
avg_incorrect_times = 0.0   # média de tempos incorretos
start_time = ""             # tempo de início em formato data

inputs_list = []            # lista de tuplos dos inputs


# função para calcular médias
def average(lst):
    if len(lst) != 0:
        return sum(lst) / len(lst)
    else:
        return 0


# função para print do dicionário
def print_dict():
    Statistics["accuracy"] = (cnt_correct_letters / (cnt_correct_letters + cnt_incorrect_letters)) * 100
    Statistics["inputs"] = inputs_list
    Statistics["number_of_hits"] = cnt_correct_letters
    Statistics["number_of_types"] = cnt_correct_letters + cnt_incorrect_letters
    Statistics["test_duration"] = cnt_time
    Statistics["test_end"] = ctime()
    Statistics["test_start"] = start_time
    Statistics["type_average_duration"] = avg_times
    Statistics["type_hit_average_duration"] = avg_correct_times
    Statistics["type_miss_average_duration"] = avg_incorrect_times

    print(Fore.GREEN + "Test completed. Results:" + Style.RESET_ALL)
    pp = pprint.PrettyPrinter(indent=4)  # usar o prettyprint para indentar
    pp.pprint(Statistics)


# número de inputs fixo
def typing_test_max_val(max_inputs):
    global cnt_letters
    global cnt_correct_letters
    global cnt_incorrect_letters
    global interm_time
    global interm_tot_time
    global avg_times
    global avg_correct_times
    global avg_incorrect_times
    global cnt_time
    global random_letter
    global typed_letter
    global inputs_list
    global start_time
    global init_time
    start_time = ctime()            # tempo inicial formato data
    init_time = time()              # tempo inicial em segundos
    interm_tot_time = init_time     # tempo intermédio total
    num_letters_to_type = max_inputs # número de letras máximo do modo (inserido pelo utilizador)

    while True:
        if cnt_letters == num_letters_to_type:
            print("You typed " + str(cnt_letters) + " letters.")
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
            elif typed_letter == " ":
                print(Fore.BLACK + Back.YELLOW + "You stopped the test!" + Style.RESET_ALL)
                exit()

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

    print_dict()


def typing_test_max_time(max_time):
    global cnt_letters
    global cnt_correct_letters
    global cnt_incorrect_letters
    global interm_time
    global interm_tot_time
    global avg_times
    global avg_correct_times
    global avg_incorrect_times
    global cnt_time
    global random_letter
    global typed_letter
    global inputs_list
    global start_time
    global init_time
    start_time = ctime()            # tempo inicial formato data
    init_time = time()              # tempo inicial em segundos
    interm_tot_time = init_time     # tempo intermédio total
    max_time_to_type = max_time    # tempo máximo do modo (inserido pelo utilizador)

    while cnt_time <= max_time_to_type:
        try:
            if cnt_time >= max_time_to_type:
                print('Current test duration ' + str(cnt_time) + ' exceeds maximum of ' + str(max_time_to_type) + " seconds.")
                break
            else:

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
                elif typed_letter == " ":
                    print(Fore.BLACK + Back.YELLOW + "You stopped the test!" + Style.RESET_ALL)
                    exit()
                else:
                    interm_time = time() - interm_tot_time
                    read_times.append(interm_time)
                    read_incorrect_times.append(interm_time)
                    interm_tot_time = time()
                    cnt_wrong_letters += 1
                    wrong_letters.append(random_letter)
                print("You typed the letter " + Fore.BLUE + typed_letter + Style.RESET_ALL)
                inputs_list.append(Input(requested=random_letter, received=typed_letter, duration=interm_time))
        except:
            print("You must define a time value first! Use -h command.")
            exit()
        cnt_time = time() - init_time


    # contabilizar tempos
    avg_times = average(read_times)
    avg_correct_times = average(read_correct_times)
    avg_incorrect_times = average(read_incorrect_times)

    print_dict()


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
        if pressed_continue:
            typing_test_max_time(args["max_value"])
    elif args["max_value"]:
        print("Test running up to " + str(args["max_value"]) + " inputs.")
        print("Press any key to start...")
        pressed_continue = readchar.readkey()
        if pressed_continue:
            typing_test_max_val(args["max_value"])
    else:
        print("No mode selected! Please use -h command.")


if __name__ == '__main__':
    main()
