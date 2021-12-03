#!/usr/bin/python3

import rospy
from bringup_exemple.msg import Dog


def callback(msg):
    rospy.loginfo(f'Received a dog name {msg.name} which is {msg.age} years old')


def main():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("chatter", Dog, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
