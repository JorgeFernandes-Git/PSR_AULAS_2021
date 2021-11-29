#!/usr/bin/python3

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


if __name__ == '__main__':
    main()
