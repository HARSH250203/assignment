#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

class LaserScanFilter:
    def __init__(self):

        rospy.init_node('laser_scan_filter', anonymous=True)


        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)


        self.filtered_pub = rospy.Publisher('/filtered_scan', LaserScan, queue_size=10)

  
        self.min_angle = 0  # Radians
        self.max_angle = 120 * (3.14159 / 180)  # Convert degrees to radians

    def scan_callback(self, data):
       

        
        min_index = int((self.min_angle - data.angle_min) / data.angle_increment)
        max_index = int((self.max_angle - data.angle_min) / data.angle_increment)

        filtered_ranges = data.ranges[min_index:max_index]

        filtered_scan = LaserScan()
        filtered_scan.header = data.header
        filtered_scan.angle_min = self.min_angle
        filtered_scan.angle_max = self.max_angle
        filtered_scan.angle_increment = data.angle_increment
        filtered_scan.time_increment = data.time_increment
        filtered_scan.scan_time = data.scan_time
        filtered_scan.range_min = data.range_min
        filtered_scan.range_max = data.range_max
        filtered_scan.ranges = filtered_ranges

        self.filtered_pub.publish(filtered_scan)

    def start(self):
        # Keep the node running
        rospy.spin()

if __name__ == '__main__':
    try:
        laser_filter = LaserScanFilter()
        laser_filter.start()
    except rospy.ROSInterruptException:
        pass

