#!/usr/bin/python3

import rospy
from bringup_exemple.msg import Dog


def main():
    rospy.init_node("publisher", anonymous=True)
    pub = rospy.Publisher("chatter", Dog, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        # create a dog message to send
        dog = Dog()
        dog.name = "bobby"
        dog.age = 77
        dog.color = "brown"
        dog.brothers.append("Rex")
        dog.brothers.append("Max")
        dog.brothers.append("Snoopy")

        rospy.loginfo(f'Publishing dog message with name {dog.name}')
        pub.publish(dog)
        rate.sleep()

        # commands for terminal
        # rosrun bringup_exemple publisher.py __name:=my_publisher
        # rosrun bringup_exemple publisher.py __name:=my_publisher chatter:=my_topic


if __name__ == '__main__':
    main()
