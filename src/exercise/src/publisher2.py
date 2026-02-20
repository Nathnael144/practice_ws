import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class HelloWorldpublisher(Node):
     def __init__(self):
         super().__init__("helloworldpub")
         self.pub=self.create_publisher(String,"helloworld",10)
         self.timer=self.create_timer(1,self.hellopublisher)
            
    
    
     def hellopublisher(self):
        msg=String()
        msg.data="Hello_world"
        self.pub.publish(msg)
        


def main(args=None):
    rclpy.init(args=args)
    my_pub=HelloWorldpublisher()
    print("The node is starting ...")
    

    try:
        rclpy.spin(my_pub)
    except KeyboardInterrupt:
        print("node terminating ...")
        




if __name__=="__main__":
    main()
