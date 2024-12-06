# bot_control Package

This package contains a Python script to read laser scan data from the `/scan` topic, filter it to a field of view between 0 to 120 degrees, and publish the filtered data to the `/filtered_scan` topic. The launch file starts both the filtering script and RViz for visualizing the filtered scan.

## Dependencies
Make sure you have the following ROS dependencies installed:

- `rospy`
- `std_msgs`
- `geometry_msgs`
- `sensor_msgs`
- `rviz`

## How to Use

### 1. Build the package
After creating the package, ensure your workspace is built.

```bash
cd ~/harsh25_ws
catkin_make

