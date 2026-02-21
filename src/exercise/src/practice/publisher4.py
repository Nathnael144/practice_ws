
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class hellopub(Node):
    def __init__(self):
        super().__init__("helloworldpub")
        self.pub=self.create_publisher(String, "helloworld",10)
        self.timer= self.create_timer(1,self.hellopublisher)




    def hellopublisher(self):
        msg=String()
        msg.data="Hello_World"
        self.pub.publish(msg)
        



def main(args=None):
    rclpy.init(args=args)
    my_pub= hellopub()
    rclpy.spin(my_pub)
    
    

if __name__=="__main__":
    main()