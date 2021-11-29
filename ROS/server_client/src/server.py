#!/usr/bin/python3

import rospy
from pub_sub_dog_class.srv import SetDogName, SetDogNameResponse


def handle_set_dog_name(req):
    return SetDogNameResponse(req.new_name)


def main():
    rospy.init_node("SetDogName")
    s = rospy.Service('SetDogName', SetDogName, handle_set_dog_name)
    rospy.spin()


if __name__ == '__main__':
    main()
