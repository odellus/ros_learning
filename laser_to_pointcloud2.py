#! /usr/bin/env python
# -*- coding: utf-8

import sensor_msgs.point_cloud2 as pc2
import rospy
from sensor_msgs.msg import PointCloud2, LaserScan
import laser_geometry.laser_geometry as lg
import math

rospy.init_node("laserscan_to_pointcloud")

lp = lg.LaserProjection()

pc_pub = rospy.Publisher("converted_pc", PointCloud2, queue_size=1)

def scan_cb(msg):
    # convert the message of type LaserScan to PointCloud2
    pc2_msg = lp.projectLaser(msg)

    # now we can do something with the PointCloud2 for example:
    # publish it
    pc_pub.publish(pc2_msg)

    # convert it to a generator of the individual points
    point_generator = pc2.read_points(pc2_msg)

    # Now we can access generator in a loop
    sum = 0.
    num = 0
    for point in point_generator:
        if not math.isnan(point[2]):
            sum += point[2]
            num += 1

    # we can calculate the average z value for example.
    print(str(sum/num))

    # or a list of individual points which is less efficient
    point_list = pc2.read_points_list(pc2_msg)

    # we can access point list with an index, each elem is namedtuple
    # we can access the elements by name. generator does not yield namedtuples
    print(point_list[len(point_list)/2].x)

rospy.Subscriber("/scan", LaserScan, scan_cb, queue_size=1)
rospy.spin()
