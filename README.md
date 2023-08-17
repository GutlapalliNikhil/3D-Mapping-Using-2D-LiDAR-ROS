# Simulating and Mapping 3D Environments with 2D Lidar in ROS

Welcome to the repository for our project that explores the world of 3D mapping using 2D Lidar in ROS (Robot Operating System). This project focuses on creating a simulated environment, collecting data with a 2D Lidar, and generating 3D maps using ROS and Gazebo.

![Project Demo](https://github.com/GutlapalliNikhil/3D-Mapping-Using-2D-LiDAR-ROS/assets/33520288/69440bef-f2df-42ef-a26f-548203eebb40)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

In this project, we designed a robot with a 2D Lidar using SolidWorks and created a URDF model to simulate it in Gazebo. The robot has a 2D Lidar that scans the environment, and we developed a Lidar plugin to collect scan data. We then processed this data to generate 3D maps using the octomap library.

## Installation

Follow these steps to set up the project locally:

```bash
git clone https://github.com/GutlapalliNikhil/3D-Mapping-Using-2D-LiDAR-ROS.git
cd 3D-Mapping-Using-2D-LiDAR-ROS/src
git clone https://github.com/OctoMap/octomap_mapping.git
git clone https://github.com/OctoMap/octomap_msgs.git
git clone https://github.com/OctoMap/octomap_ros.git
cd ..
catkin_make
```

## Usage

1.Launch the Gazebo simulation with the robot model:

```bash
roslaunch Assem1 testing.launch
```

2. Send the values to the servo motor:

```bash
rosrun Assem1 lidar_control_node.py
```

3. Convert the laserscan to pointcloud:

```bash
rosrun Assem1 laserscan_to_pointcloud.py
```

4. Run the Octomap to get the map:

```bash
roslaunch octomap_server octomap_mapping.launch
```

## Contributing

I welcome contributions to improve this project. If you find any issues or have suggestions for enhancements, feel free to submit a pull request or open an issue.
