#!/usr/bin/python3

from collections import namedtuple
import pprint
from time import time, ctime

Input = namedtuple("Input", ["requested", "received", "duration"])
my_dict = {
    "accuracy": 0.0,
    "inputs": [],
    "number_of_hits": 0,
    "number_of_types": 0,
    "test_duration": 0.0,
    "test_end": "",
    "test_start": "",
    "type_average_duration": 0.0,
    "type_hit_average_duration": 0.0,
    "type_miss_average_duration": 0.0
}


def main():
    # input tuples
    a = Input(requested="w", received="d", duration=2.3)
    b = Input(requested="r", received="f", duration=1.5)
    c = Input(requested="i", received="y", duration=1.5)

    my_dict["accuracy"] = 2.8
    my_dict["inputs"] = [a, b, c]
    my_dict["number_of_hits"] = 5
    my_dict["number_of_types"] = 8
    my_dict["test_duration"] = 5.8
    my_dict["test_end"] = ctime()
    my_dict["test_start"] = ctime()
    my_dict["type_average_duration"] = 2.6
    my_dict["type_hit_average_duration"] = 1.5
    my_dict["type_miss_average_duration"] = 5.4

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(my_dict)


if __name__ == '__main__':
    main()
