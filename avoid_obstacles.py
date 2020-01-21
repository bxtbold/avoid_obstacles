#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
  global g_range_ahead
  g_range_ahead = min(msg.ranges)

g_range_ahead = 1                                                   #initializing the distance from the robot to an obstacle
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)       # subscribing and getting msg from a sensor
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)       # publishing and defininf the speed with Twist

rospy.init_node('avoid_obstacles')      # creating node and naming it avoid_obstacles

# state_change_time = rospy.Time.now()
driving_forward = True                  # when true, the robot drives forward
rate = rospy.Rate(5)                    # sending data with 5 hertz 
twist = Twist()                         # using the class Twist() as twist

while not rospy.is_shutdown():
    if driving_forward:
        if g_range_ahead < 0.8:         # if the obstacle gets closer aroudn 0.8
            driving_forward = False     # stops
        else:
            pass
        
        

        
    
    
    
    
    
    
    cmd_vel_pub.publish(twist)          # publishing 
    rate.sleep()                        # end of the loop
















