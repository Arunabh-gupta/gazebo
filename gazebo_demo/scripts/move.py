#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64
import random
import math

def main():
    rate = rospy.Rate(10) # 10hz
    lpos = 0
    rpos = 0
    left_pub = rospy.Publisher("/bot/joint1_position_controller/command",
                                            Float64, queue_size=10)
    right_pub = rospy.Publisher("/bot/joint2_position_controller/command",
                                            Float64, queue_size=10)
    while not rospy.is_shutdown():

        lpos += random.random()
        rpos += random.random()
        if random.randint(0, 4) != 0:
            left_pub.publish(lpos)
        if random.randint(0, 4) != 0:
            right_pub.publish(rpos)

        rate.sleep()

if __name__ == '__main__':
    rospy.init_node("move_node", anonymous=True)
    try:
        main()
    except rospy.ROSInterruptException:
        pass

