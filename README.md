oryx
====

This repo maintains the a collection of ROS packages for the Oryx platform.
All packages are in the root directory of the repository.

Development
-----------
Checkout the repository to the src directory of the catkin worksapce (`${catkin_workspace}/src/oryx`). To build the packages return to the catkin workspace directory and then run `catkin_make`. To do a clean build run `rm -r build devel`.

The development branch is the 'in-flux' version of the master branch. Code which has been at least tested for basic functionality, but not for full validation, should be merged into this branch.

When creating/modify data for the development branch, create a new 'topic' branch off of development that will contain all of your commits as you work on your modifcations. Once your work is finished and gone through basic testing, merge it back into the development branch.


Packages
--------
- **epos\_manager**: A package containing nodes needed for communicating with Maxon Epos motor controllers
- **oryx**: A meta package for all of the oryx packages
- **oryx\_diagnostics**: A node for monitoring other nodes
- **oryx\_gui**: A package containing a basic teleop GUI (rosbuild)
- **oryx\_manager**: A package which contains all of the high level operation nodes for oryx
- **oryx\_msgs**: A package containing all of the messages used by the oryx packages
- **oryx\_network\_manager**: A package which allows for remote management of network interfaces and automatic network configuration

Other Projects
--------------
- **AxisCamera**: A java library for controlling axis cameras over http
- **AxisCameraGUI**: A java ui for controlling axis cameras
