#!/usr/bin/python3
# license removed for brevity
import rospy
from std_msgs.msg import String


def main():
    pub = rospy.Publisher('A1', String, queue_size=10)
    rospy.init_node('Aveiro', anonymous=True)
    rate = rospy.Rate(1)  # 10hz
    while not rospy.is_shutdown():
        hello_str = "Here goes a car at " + str(rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
