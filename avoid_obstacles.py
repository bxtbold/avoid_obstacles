#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from turn import turn_right,turn_left
from go_forward import go_forward
from scan_callback import callback


range_ahead = 1.5     # initializing the distance from the robot to an obstacle

scan_sub = rospy.Subscriber('scan', LaserScan, callback)       # subscribing and getting msg from a sensor
vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)           # publishing and defininf the speed with Twist

rospy.init_node('avoid_obstacles')      # creating node and naming it avoid_obstacles

go_forward = True                  			# when True, the robot drives forward
rate = rospy.Rate(5)                    # sending data with 5 hertz 

go = Twist()                            # using the class Twist() as twist

while not rospy.is_shutdown():
	if go_forward:
		if range_ahead < 0.8:      # if the obstacle gets closer than 0.8 m
			go_forward = False       # stops
		else:
			pass			

	if go_forward:
    go.linear.x = 1
  else:
    pass			# turn either right or left

  cmd_vel_pub.publish(twist)
	vel_pub.publish(go)         	
	rate.sleep()                     
