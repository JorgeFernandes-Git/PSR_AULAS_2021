#!/usr/bin/python3
import argparse
import rospy
from std_msgs.msg import String
from pub_sub_dog_class.msg import Dog


def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + " Message Received: " + str(msg.name))
    rospy.loginfo(rospy.get_caller_id() + " Message Received: " + str(msg.age))
    rospy.loginfo(rospy.get_caller_id() + " Message Received: " + str(msg.color))
    rospy.loginfo(rospy.get_caller_id() + " Message Received: " + str(msg.brothers))


def main():
    rospy.init_node("Casa")
    rospy.Subscriber("Carro", Dog, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
