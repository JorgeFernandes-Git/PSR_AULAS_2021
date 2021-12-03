#!/usr/bin/python3


import rospy
from bringup_exemple.msg import Dog
from colorama import Fore, Back, Style


def main():
    rospy.init_node("publisher", anonymous=True)
    pub = rospy.Publisher("chatter", Dog, queue_size=1)
    # frequency
    frequency = rospy.get_param("~frequency", default=1)  # "~" means private param
    rate = rospy.Rate(frequency)  # 10hz

    while not rospy.is_shutdown():
        # read param
        highlight_text_color = rospy.get_param("/highlight_text_color")

        # create a dog message to send
        dog = Dog()
        dog.name = "bobby"
        dog.age = 77
        dog.color = "brown"
        dog.brothers.append("Rex")
        dog.brothers.append("Max")
        dog.brothers.append("Snoopy")

        rospy.loginfo(f'Publishing dog message with name '
                      f'{getattr(Fore, highlight_text_color) + dog.name + Style.RESET_ALL}')
        pub.publish(dog)
        rate.sleep()

        # commands for terminal
        # rosrun bringup_exemple publisher.py __name:=my_publisher
        # rosrun bringup_exemple publisher.py __name:=my_publisher chatter:=my_topic

        # edit param in ROS
        # rosparam set highlight_text_color GREEN
        # rosparam set /my_publisher/frequency

        # rosparam list and rosparam get

        # rosparam load params.yml -- run in director roscd package_name/params folder


if __name__ == '__main__':
    main()
