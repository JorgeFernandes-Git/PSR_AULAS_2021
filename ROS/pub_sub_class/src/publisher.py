#!/usr/bin/python3
import argparse
import rospy
from std_msgs.msg import String
from pub_


def main():
    parser = argparse.ArgumentParser(description='Select the message to send, the topic and the rate')
    parser.add_argument("-nd", "--node", type=str, default="Anywhere", help="Name the node to publish")
    parser.add_argument('-msg', '--message', type=str, default="No message to send", help='Message to send')
    parser.add_argument('-tp', '--topic', type=str, default="Anywhere", help='Topic to send message')
    parser.add_argument('-rt', '--rate', type=float, default=0.5, help='Message rate')
    args = vars(parser.parse_args())

    rospy.init_node(args["node"], anonymous=True)
    pub = rospy.Publisher(args["topic"], String, queue_size=10)
    rate = rospy.Rate(args["rate"])  # 10hz

    while not rospy.is_shutdown():
        message_to_send = args["message"]
        rospy.loginfo(message_to_send)
        pub.publish(message_to_send)
        rate.sleep()


if __name__ == '__main__':
    main()
