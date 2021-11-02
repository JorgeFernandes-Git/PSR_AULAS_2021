#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to print hello world!
# Miguel Riem Oliveira.
# PSR, Setember 2020.
# --------------------------------------------------
import random
import time
import readchar
from colorama import Fore, Style
import argparse
from collections import namedtuple
from pprint import pprint


Input = namedtuple('Input', ['Requested', 'Received'])

Statistics={'Accuracy': 0.0, 'Inputs': [], 'Number_of_Hits': 0, "Number_of_Types": 0, 'Test_Start': '', 'Test_End': '', 'Test_Duration': 0.0, 'Type_Average_Duration': 0.0, "Type_Hit_Average_Duration": 0.0, "Type_Miss_Average_Duration": 0.0}

letters = "abcdefghijklmnopqrstuvwxyz"

def tic():
    seconds = time.time()
    tempo_atual = time.localtime(seconds)
    tempo_segundos = time.mktime(tempo_atual)
    return seconds


def tac():
    seconds = time.time()
    tempo_atual = time.localtime(seconds)
    tempo_segundos = time.mktime(tempo_atual)
    return seconds

def modo_tempo(x):
    count = 0
    tempo_start = tic()
    tempo_final = 0
    count = 0
    hits = 0
    key = []  # Lista para os inputs
    average_hits = []
    average_miss = []

    seconds = time.time()
    tempo_inicio = time.ctime(seconds)
    tempo_segundos_inicio = tic()

    while tempo_final - tempo_start < x:
        average_inicio = tic()
        letra = random.choice(letters)
        tempo_final = tac()

        print("Type the letter " + Fore.YELLOW + str(letra) + Style.RESET_ALL)
        pressed_key = readchar.readkey()
        key.append(Input(letra, pressed_key))

        if pressed_key == letra:
            print("You pressed " + Fore.GREEN + pressed_key + Style.RESET_ALL)
            tempo_hit = tac()
            duration_hit = tempo_hit - average_inicio
            average_hits.append(duration_hit)
            hits += 1
        elif pressed_key == ' ':
            break

        else:
            print("You pressed " + Fore.RED + pressed_key + Style.RESET_ALL)
            tempo_miss = tac()
            duration_miss = tempo_miss - average_inicio
            average_miss.append(duration_miss)
        count += 1

    accuracy = hits / count

#Este bloco de código determina a data de fim em segundos e data, e faz a diferença entre a de inicio, para determinar a duração em segundos do teste
    seconds = time.time()
    tempo_fim = time.ctime(seconds)
    tempo_segundos_fim = tac()
    duration = tempo_segundos_fim - tempo_segundos_inicio

#Calcula a média do tempo dos hits
    media_right = 0
    for x in range(0, len(average_hits)):
        media_right = media_right + average_hits[x]
    if len(average_hits) > 0:
        media_right = media_right / len(average_hits)
    else:
        media_right = 0.0

#Calcula a média do tempo para os miss
    media_miss = 0
    for x in range(0, len(average_miss)):
        media_miss = media_miss + average_miss[x]
    if len(average_miss) > 0:
        media_miss = media_miss / len(average_miss)
    else:
        media_miss = 0.0

    Statistics['Accuracy'] = accuracy
    Statistics['Test_Duration'] = duration
    Statistics['Test_Start'] = tempo_inicio
    Statistics['Test_End'] = tempo_fim
    Statistics['Number_of_Hits'] = hits
    Statistics['Number_of_Types'] = count
    Statistics['Inputs'] = key
    Statistics['Type_Hit_Average_Duration'] = media_right
    Statistics['Type_Miss_Average_Duration'] = media_miss


def modo_teclas(x):
    count = 0
    hits=0
    key=[] #Lista para os inputs
    average_hits = []
    average_miss = []

#Este bloco determina a data de inicio em segundos e em data
    seconds = time.time()
    tempo_inicio = time.ctime(seconds)
    tempo_segundos_inicio = tic()

    while count < x:
        average_inicio = tic()
        letra = random.choice(letters)
        print("Type the letter " +  Fore.YELLOW + str(letra) + Style.RESET_ALL)
        pressed_key = readchar.readkey()
        key.append(Input(letra, pressed_key))

        if pressed_key == letra:
            print("You pressed " + Fore.GREEN + pressed_key + Style.RESET_ALL)
            tempo_hit = tac()
            duration_hit = tempo_hit - average_inicio
            average_hits.append(duration_hit)
            hits += 1
        elif pressed_key == ' ':
            break

        else:
            print("You pressed " + Fore.RED + pressed_key + Style.RESET_ALL)
            tempo_miss = tac()
            duration_miss = tempo_miss - average_inicio
            average_miss.append(duration_miss)
        count += 1

    accuracy = hits/count

#Este bloco de código determina a data de fim em segundos e data, e faz a diferença entre a de inicio, para determinar a duração em segundos do teste
    seconds = time.time()
    tempo_fim = time.ctime(seconds)
    tempo_segundos_fim = tac()
    duration = tempo_segundos_fim - tempo_segundos_inicio

#Calcula a média do tempo dos hits
    media_right = 0
    for x in range(0, len(average_hits)):
        media_right = media_right + average_hits[x]
    if len(average_hits) > 0:
        media_right = media_right / len(average_hits)
    else:
        media_right = 0.0

#Calcula a média do tempo para os miss
    media_miss = 0
    for x in range(0, len(average_miss)):
        media_miss = media_miss + average_miss[x]
    if len(average_miss) > 0:
        media_miss = media_miss / len(average_miss)
    else:
        media_miss = 0.0


    Statistics['Accuracy'] = accuracy
    Statistics['Test_Duration'] = duration
    Statistics['Test_Start'] = tempo_inicio
    Statistics['Test_End'] = tempo_fim
    Statistics['Number_of_Hits'] = hits
    Statistics['Number_of_Types'] = count
    Statistics['Inputs'] = key
    Statistics['Type_Hit_Average_Duration'] = media_right
    Statistics['Type_Miss_Average_Duration'] = media_miss


def main():
    parser = argparse.ArgumentParser(description=' PSR typing test ')
    parser.add_argument('-mv', '--max_value', type=int,
                        help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.')
    parser.add_argument('-utm', '--use_time_mode', type=bool, help='Defines if time mode is used.')

    args = vars(parser.parse_args())
    print(args)

    print("Typing test PSR. Press any key to begin the test")
    pressed_continue = readchar.readkey()
    if pressed_continue:
        if args['use_time_mode']:
            modo_tempo(args['max_value'])
        elif args['max_value']:
            modo_teclas(args['max_value'])
        else:
            print('No mode selected')

    print(Fore.BLUE + "You finished the test, here are your results:" + Style.RESET_ALL)
    pprint(Statistics)


if __name__ == "__main__":
    main()


