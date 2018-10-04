# Unit 2: Topics

Still using the turtlebot.

- We'll learn what ROS topics are and how to manage them.  
- Learn what a publisher is and how we create one.  
- Learn what topic messages are and how they work. This is pretty much what there is to ROS. It's a framework for constructing structured message templates to pass between devices.

### Part 1: Publisher

```python
#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/counter', Int32, queue_size=1)
rate = rospy.Rate(2)
count = Int32()
count.data = 0

while not rospy.is_shutdown():
  pub.publish(count)
  count.data += 1
  rate.sleep()
```
