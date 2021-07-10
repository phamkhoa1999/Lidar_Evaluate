#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan 
f = 0.0
b = 0.0
r = 0.0
l = 0.0   
def Scan_callback(msg):
     
       f = msg.ranges[1]
       b = msg.ranges[len(msg.ranges)/2]
       r = msg.ranges[270]
       l = msg.ranges[90]  
       #print " f = " + str(f) + " b = " + str(b) + " r = " + str(r) + " l = " + str(l)
       print " b = " + str(b)
       #if f < 0.5:  
        #print "Front Obstacle"
       #if b < 0.5: 
        #print "Back Obstacle"
       #if r < 0.5: 
        #print "Right Obstacle"
       #if l < 0.5: 
        #print "Left Obstacle"       
rospy.init_node('Sub', anonymous=True)
sub = rospy.Subscriber("scan",LaserScan, Scan_callback)
rospy.spin() 

