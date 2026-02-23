#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class rpmsubscriber(Node):
    def __init__(self):
        super().__init__("rpmsub")
        self.sub=self.create_subscription(Float32, "wheel_rpm",self.listener_callback,10)
    def listener_callback(self, msg):
        print(msg.data)
        




def main(args=None):
    rclpy.init(args=args)
    my_sub= rpmsubscriber()
    print("The subscriber is listening")
    rclpy.spin(my_sub)
    
    




if __name__=="__main__":
    main()