#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def lidar_control():
    rospy.init_node('lidar_control_node', anonymous=True)
    pub = rospy.Publisher('/r2d2_head_controller/command', Float64, queue_size=10)
    rate = rospy.Rate(30)  # 1 Hz
    
    angle = 0.0
    increment = 0.01
    max_angle = 0.4
    direction = 1  # 1 for incrementing, -1 for decrementing
    
    while not rospy.is_shutdown():
        angle_1 = -angle
        pub.publish(angle_1)
        
        if direction == 1:
            angle += increment
            if angle > max_angle:
                direction = -1
        else:
            angle -= increment
            if angle < 0:
                direction = 1
        
        rate.sleep()

if __name__ == '__main__':
    try:
        lidar_control()
    except rospy.ROSInterruptException:
        pass

