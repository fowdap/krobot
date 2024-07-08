from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions
from launch.actions import DeclareLaunchArgument
import os

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'
        ),
        launch_ros.actions.Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[
                os.path.join(
                    get_package_share_directory("my_robot_localization"), 
                    'config', 
                    'ekf.yaml'
                ),
                {'use_sim_time': True}
            ],
        ),
    ])
