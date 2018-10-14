#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print("Ranges:")
    print(msg.ranges)
    print("Intensities:")
    print(msg.intensities)

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('scan', LaserScan, callback)
rospy.spin()

