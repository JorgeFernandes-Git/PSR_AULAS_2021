#!/usr/bin/python3
import argparse
import rospy
from std_msgs.msg import String
from bringup_exemple.msg import Dog


def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + " Message Received: " + str(msg.name))
    rospy.loginfo(rospy.get_caller_id() + " Message Received: " + str(msg.age))
    rospy.loginfo(rospy.get_caller_id() + " Message Received: " + str(msg.color))
    rospy.loginfo(rospy.get_caller_id() + " Message Received: " + str(msg.brothers))

def main():
    parser = argparse.ArgumentParser(description='Select the node and the topic to subscribe')
    parser.add_argument('-nd', '--node', type=str, default="Lost", help='Name a node to subscribe')
    parser.add_argument('-tp1', '--topic1', type=str, help='Name a topic1')
    parser.add_argument('-tp2', '--topic2', type=str, help='Name a topic2')
    args = vars(parser.parse_args())

    rospy.init_node(args["node"], anonymous=True)
    rospy.Subscriber(args["topic1"], Dog, callback)

    if not args["topic2"] is None:
        rospy.Subscriber(args["topic2"], Dog, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
