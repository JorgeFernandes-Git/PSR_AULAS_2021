#!/usr/bin/python3

import rospy
from pub_sub_dog_class.msg import Dog
from pub_sub_dog_class.srv import SetDogName, SetDogNameResponse


def handle_set_dog_name(req):
    return SetDogNameResponse(req.new_name)


def main():
    rospy.init_node("SetDogName")
    pub = rospy.Publisher("Carro", Dog, queue_size=10)
    rate = rospy.Rate(1)  # 10hz

    while not rospy.is_shutdown():
        dog = Dog()
        dog.name = rospy.Service('SetDogName', SetDogName, handle_set_dog_name)
        dog.age = 77
        dog.color = "brown"
        dog.brothers.append("Rex")
        dog.brothers.append("Max")
        dog.brothers.append("Snoopy")

        # message_to_send = args["message"]
        rospy.loginfo("Sending a dog ...")
        pub.publish(dog)
        rate.sleep()

    rospy.spin()


if __name__ == '__main__':
    main()
