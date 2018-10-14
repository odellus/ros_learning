Then they walk us through  making a simple_topic_subscriber

```python
#! /usr/bin/env python

import rospy
from std_msgs import Int32

def callback(msg):
    print(msg.data)

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('counter', Int32, callback)
rospy.spin()
```

They want us to investigate the `/odom` topic so you can figure out what message the `/odom` topic.

Then they want us to create a new message called `Age.msg` to keep track of how long the robot has been spawned.


I. find_packages()

```cmake
find_package(catkin REQUIRED COMPONENTS
       rospy
       std_msgs
       message_generation   # Add message_generation here, after the other packages
)
```

II. add_message_file()
```cmake
add_message_files(
      FILES
      Age.msg
    ) # Dont Forget to UNCOMENT the parenthesis and add_message_files TOO
```

III. generate_messages()
```cmake
generate_messages(
      DEPENDENCIES
      std_msgs
) # Dont Forget to uncoment here TOO
```

IV. catkin_package()
```cmake
catkin_package(
      CATKIN_DEPENDS rospy message_runtime   # This will NOT be the only thing here
)
```

So the whole thing looks sort of like this:
```cmake
cmake_minimum_required(VERSION 2.8.3)
project(topic_ex)


find_package(catkin REQUIRED COMPONENTS
  std_msgs
  message_generation
)

add_message_files(
  FILES
  Age.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)


catkin_package(
  CATKIN_DEPENDS rospy message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
```

Modify package.xml by adding these two lines
```xml
<build_depend>message_generation</build_depend>
<run_depend>message_runtime</run_depend>
```

```xml
<?xml version="1.0"?>
<package>
  <name>topic_ex</name>
  <version>0.0.0</version>
  <description>The topic_ex package</description>


  <maintainer email="user@todo.todo">user</maintainer>

  <license>TODO</license>

 <buildtool_depend>catkin</buildtool_depend>
  <build_depend>rospy</build_depend>
  <build_depend>message_generation</build_depend>
  <run_depend>rospy</run_depend>
  <run_depend>message_runtime</run_depend>

  <export>

  </export>
</package>
```

then you
```bash
roscd; cd ..
catkin_make
source devel/setup.bash
```

then you can `rosmsg show Age` to see
```bash
user ~ $ rosmsg show Age
[topic_ex/Age]:
float32 years
float32 months
float32 days
```
So they have us do a

1. Create a Publisher that writes into the /cmd_vel topic in order to move the robot.
2. Create a Subscriber that reads from the /kobuki/laser/scan topic. This is the topic where the laser publishes its data.
3. Depending on the readings you receive from the laser's topic, you'll have to change the data you're sending to the /cmd_vel topic, in order to avoid the wall. This means, use the values of the laser to decide.

They send us to a few urls to learn more.
1. http://wiki.ros.org/Topics
2. http://wiki.ros.org/Messages
3. http://wiki.ros.org/msg
4. http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
5. http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber
