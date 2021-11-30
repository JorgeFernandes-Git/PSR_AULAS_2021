#!/usr/bin/python3

import sys
import rospy
from pub_sub_dog_class.srv import *


def main(new_name):
    rospy.wait_for_service('SetDogName')
    try:
        set_dog_name = rospy.ServiceProxy('SetDogName', SetDogName)
        resp1 = set_dog_name(new_name)
        return resp1.result
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def usage():
    return "%s Dog name" % sys.argv[0]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        new_name = str(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
