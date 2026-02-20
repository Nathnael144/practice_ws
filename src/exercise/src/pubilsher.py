import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class HelloworldPublisher(Node):
    def __init__(self):
        super().__init__("helloworld_publisher")
        self.pub= self.create_publisher(String,"hello_world",10)
        self.timer= self.create_timer(1,self.publish_hello_world)
        self.counter=0
    def publish_hello_world(self):
        msg=String()
        msg.data="Hello_World"
        self.pub.publish(msg)
        self.counter+=1






def main(args=None):
    rclpy.init(args=args)
    my_pub=HelloworldPublisher()
    print("publisher node running....")

    try:
        rclpy.spin(my_pub)
    except KeyboardInterrupt:
        print("terminating node...")



if __name__=="__main__":
    main()
   
