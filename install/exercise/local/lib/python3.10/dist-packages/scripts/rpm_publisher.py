#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class rpmpublisher(Node):
    def __init__(self):
        super().__init__("wheelrpm")
        self.pub= self.create_publisher(Float32, "wheel_rpm",10)
        self.timer= self.create_timer(1,self.rpm_publisher)
    def rpm_publisher(self):
        msg= Float32()
        msg.data = 20.1
        self.pub.publish(msg)
        
            




def main(args=None):
    rclpy.init(args=args)
    my_pub= rpmpublisher()
    print("The publisher node is running")
    rclpy.spin(my_pub)
    my_pub.destroy_node()
    rclpy.shutdown()
    





if __name__== "__main__":
    main()