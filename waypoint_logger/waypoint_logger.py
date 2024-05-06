from rclpy.node import Node
import rclpy
import numpy as np
from nav_msgs.msg import Odometry
from numpy import linalg as LA
from tf_transformations import euler_from_quaternion
from os.path import expanduser
from time import gmtime, strftime


class WaypointLogger(Node):

    def __init__(self):
        super().__init__("waypoint_logger")
        home = expanduser('~')
        self.file = open(strftime( home+ '/rcws/logs/wp-%Y-%m-%d-%H-%M-%S',gmtime())+'.csv', 'w')
        self.create_subscription(Odometry, "pf/pose/odom", self.save_waypoint, 10)
        self.get_logger().info("node initialized")

    def save_waypoint(self, data):

        quaternion = np.array([data.pose.pose.orientation.x, 
                            data.pose.pose.orientation.y, 
                            data.pose.pose.orientation.z, 
                            data.pose.pose.orientation.w])

        euler = euler_from_quaternion(quaternion)
        speed = LA.norm(np.array([data.twist.twist.linear.x, 
                                data.twist.twist.linear.y, 
                                data.twist.twist.linear.z]),2)
        if data.twist.twist.linear.x>0.:
            self.get_logger().info("data.twist.twist.linear.x")

        self.file.write('%f, %f, %f, %f\n' % (data.pose.pose.position.x,
                                        data.pose.pose.position.y,
                                        euler[2],
                                        speed))
        

if __name__ == "__main__":

    rclpy.init()
    rclpy.spin(WaypointLogger())
    rclpy.shutdown()
    print("exiting")

