#!/usr/bin/python3


import argparse
import json

import cv2 as cv
import numpy as np

def main():

    # parse the json file with BGR limits (from color_segmenter.py)
    parser = argparse.ArgumentParser(description="Load a json file with limits")
    parser.add_argument("-j", "--json", type=str, required=True, help="Full path to json file")
    args = vars(parser.parse_args())

    # read the json file
    with open(args["json"], "r") as file_handle:
        data = json.load(file_handle)

    # print json file then close
    print(data)
    file_handle.close()


if __name__ == '__main__':
    main()