ouster_description
===================

This package is forked from https://github.com/clearpathrobotics/ouster_description.git.

In order to use this description for integrating OS1-128 with the prius, I have included an additional urdf file for this sensor. For the rest, this package is exactly the same as the package from clearpathrobotics.

Example use
------------

To add the lidar to a robot, the easiest way is to clone both this repo and https://github.com/ouster-lidar/ouster_example
into your workspace and build as normal.

Then create an accessories URDF file and point e.g. JACKAL_URDF_EXTRAS to point to it.  For example, this will
add the lidar to a Jackal's front mount:

    <?xml version="1.0"?>
    <robot xmlns:xacro="http://www.ros.org/wiki/xacro">
      <xacro:include filename="$(find ouster_description)/urdf/OS1-128.urdf.xacro" />
      <xacro:OS1-128 parent="base_link">
        <origin xyz="0 0 0" rpy="0 0 0" />
      </xacro:OS1-128>
    </robot>
