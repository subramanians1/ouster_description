from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    urdf_file = PathJoinSubstitution([
        FindPackageShare("ouster_description"),
        "urdf",
        "OS1-128.urdf.xacro"
    ])

    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            arguments=[urdf_file]
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", PathJoinSubstitution([
                FindPackageShare("ouster_description"),
                "rviz",
                "example.rviz"
            ])]
        ),
    ])
