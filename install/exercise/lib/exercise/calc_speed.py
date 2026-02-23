#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

wheel_radius=30/100  # wheel radius in meters (30 cm converted to meters)

class rpmsubscriber(Node):
    def __init__(self):
        super().__init__("rpm")
        self.sub=self.create_subscription(Float32, "wheel_rpm",self.calculate_speed,10)
        self.pub=self.create_publisher(Float32, "wheel_speed",10)
    def calculate_speed(self, rpm_msg):
        speed= rpm_msg.data*wheel_radius*2*3.14/60 # speed= rpm*radius*2*pi/60
        speed_msg= Float32()
        speed_msg.data= float(speed)
        self.pub.publish(speed_msg)
        




def main(args=None):
    rclpy.init(args=args)
    my_sub= rpmsubscriber()
    print("The subscriber is listening")
    rclpy.spin(my_sub)
    
    




if __name__=="__main__":
    main()