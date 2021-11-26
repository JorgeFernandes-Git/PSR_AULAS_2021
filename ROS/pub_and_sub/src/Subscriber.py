#!/usr/bin/python3
import argparse
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " Message Received: " + str(data.data))


def main():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    parser = argparse.ArgumentParser(description='Select the node and the topic to subscribe')
    parser.add_argument('-nd', '--node', type=str, default="Lost", help='Name a node to subscribe')
    parser.add_argument('-tp1', '--topic1', type=str, default="Anywhere", help='Name a topic1')
    parser.add_argument('-tp2', '--topic2', type=str, help='Name a topic2')
    args = vars(parser.parse_args())

    rospy.init_node(args["node"], anonymous=True)
    rospy.Subscriber(args["topic1"], String, callback)

    if not args["topic2"] is None:
        rospy.Subscriber(args["topic2"], String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
