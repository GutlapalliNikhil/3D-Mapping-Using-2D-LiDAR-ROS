cmake_minimum_required(VERSION 2.8.3)

project(Assem1)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

catkin_install_python(PROGRAMS laserscan_to_pointcloud.py lidar_control_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
