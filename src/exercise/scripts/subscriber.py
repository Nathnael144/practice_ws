#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class helloworldsubscriber(Node):
    def __init__(self):
        super().__init__("helloworld_publishersu")
        self.create_subscription(String,"hello_world",self.subscriber_callback,10)
    def subscriber_callback(self,msg):
        print("recived:" + msg.data)
        
        




def main(args=None):
    rclpy.init(args=args)
    my_pub=helloworldsubscriber()
    print("wating for the data to be published ...")
    

    try:
        rclpy.spin(my_pub)
    except KeyboardInterrupt:
        print("node terminating ...")
        








if __name__=="__main__":
    main()