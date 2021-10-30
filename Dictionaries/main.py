#!/usr/bin/python3

from collections import namedtuple

Input = namedtuple("Input", ["requested", "received", "duration"])


def main():
    mydict = {
        "accuracy": 0.0,
        "inputs": [Input(requested="", received="", duration=0.0)],
        "number_of_hits": 0,
        "number_of_types": 5,
        "test_duration": 0.0,
        "test_end": "",
        "test_start": "",
        "type_average_duration": 0.0,
        "type_hit_average_duration": 0.0,
        "type_miss_average_duration": 0.0
    }

    print(mydict)


if __name__ == '__main__':
    main()
