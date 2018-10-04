# 28 September 2018

I need to work more on getting plants loaded into Gazebo and all of that jazz. I'm somewhat familiar with Gazebo since I've already done most of the ROS in 5 Days. I just keep coming up against the building block that I want to be able to run all of the demos from ROS in 5 Days locally. So that's what these notes are going to be about. Getting ROS in 5 Days to work locally.

### ROS Basics

 The first lecture is about the basics of ROS and it uses the turtlebot. And when I say basics I mean like controlling a turtlebot with the keyboard with  

 `roslaunch turtlebot_teleop keyboard_teleop.launch`  

and then going over things like the basic structure of a package

```
package directory
|--launch directory: Contains launch files
|--src directory: Source files (cpp, python)
|--CMakeLists.txt: List of cmake rules for compilation
|--package.xml: Package information and dependencies
```

Then they show you a basic launch file after having you `roscd turtlebot_teleop`
```xml
<launch>
  <!-- turtlebot_teleop_key already has its own built in velocity smoother -->
  <node pkg="turtlebot_teleop" type="turtlebot_teleop_key.py" name="turtlebot_teleop_keyboard"  output="screen">
    <param name="scale_linear" value="0.5" type="double"/>
    <param name="scale_angular" value="1.5" type="double"/>
    <remap from="turtlebot_teleop_keyboard/cmd_vel" to="/cmd_vel"/>   <!-- cmd_vel_mux/input/teleop"/-->
  </node>
</launch>
```

Then they go through the steps of creating your own package from scratch with

```bash
roscd
cd ..
pwd # To show where catkin_ws is on the filesystem.
cd src
catkin_create_pkg my_package rospy
```
and outline the structure of the command with  
`catkin_create_pkg <package_name> <package_dependecies>`

They then show how you get the input of `../duplicate_rosignite.py`


```bash
rospack list
rospack list | grep my_package
roscd my_package
```

After that it's on to creating your first ros program `src/simple.py`

```python
#! /usr/bin/env python
import rospy

rospy.init_node('HelloWorld')
print("Hello World!")
```

Then you create the launch file with
```
roscd my_package
mkdir launch
touch launch/my_package_launch_file.launch
```
and add the contents of the launch file given earlier to `my_package_launch_file.launch`

They let us know we may need to run `rospack profile` for `my_package` to show up so we can `roscd my_package` and finally:
```bash
roslaunch my_package my_package_launch_file.launch
```
Then they show that you need to `chmod +x <ros_python_code>.py` If the order of these things seems off, sorry I'm just relaying it in my notes. Void where prohibited.

Then they use the running `HelloWorld` ROS node to show off how `rosnode list` works and get us to update `simple.py` to do something more interesting and rename it `simple_loop.py`.
```python
#! /usr/bin/env python

import rospy

rospy.init_node("HelloWorld")
rate = rospy.Rate(2)               # We create a Rate object of 2Hz
while not rospy.is_shutdown():     # Endless loop until Ctrl + C
   print "Hello World!:
   rate.sleep()                    # We sleep the needed time to maintain the Rate fixed above

# This program creates an endless loop that repeats itself 2 times per second (2Hz) until somebody presses Ctrl + C
# in the Shell
```
Then they want us to launch the package again with  
`roslaunch my_package my_package_launch_file.launch`  
so we can inspect the nodes running on ROS with `rosnode list` and finally  
`rosnode info /HelloWorld` (note, the node they refer to is actually called ObiWan, but I hate Star Wars shit, so I changed it).

### Compile a package
We use `catkin_make` to compile ROS packages into executable ROS nodes. `catkin_make` apparently compiles all packages by default, but if we only want to compile the single package, we use `catkin_make --only-pkg-with-deps <package_name>`

### Parameter Server

We access the parameter server dictionary with the command `rosparam`

`rosparam list` shows all the parameters stored in the server.

`rosparam get <parameter_name>` gets the value of a certain parameter in the server while `rosparam set <parameter_name> <value>` sets the value of a parameter in the server.

### Roscore

So yeah, like `roscore` is the fundamental node that needs to be running for ROS to work.

### Environmental Variables

They want you to `export | grep ROS` so you can see what ROS env variables are set on your machine and list off a few they think are important

```bash
user ~ $ export | grep ROS
declare -x ROSLISP_PACKAGE_DIRECTORIES="/home/user/catkin_ws/devel/share/common-lisp"
declare -x ROS_DISTRO="indigo"
declare -x ROS_ETC_DIR="/opt/ros/indigo/etc/ros"
declare -x ROS_MASTER_URI="http://localhost:11311"
declare -x ROS_PACKAGE_PATH="/home/user/catkin_ws/src:/opt/ros/indigo/share:/opt/ros/indigo/stacks"
declare -x ROS_ROOT="/opt/ros/indigo/share/ros"
```
Okay so I made all these notes, but I haven't yet started working on my own machine. I guess that's my biggest gripe about the robot ignite academy. They don't show me how to set it up on my own machine.

Okay they're using gazebo 7. I think I need to follow their lead and just use gazebo 7 myself since getting it working with ROS is apparently tough without it.
