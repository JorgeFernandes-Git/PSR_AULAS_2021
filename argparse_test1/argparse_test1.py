#!/usr/bin/python3


import argparse


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
    else:
        print("Not using time mode. Test will ask for " + str(args["max_value"]) + " responses")


if __name__ == '__main__':
    main()
