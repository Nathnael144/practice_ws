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

# --- Explanation ---
# This script defines a ROS 2 publisher node using rclpy (Python client library for ROS 2).
#
# 1. The class HelloWorldpublisher inherits from Node and initializes a publisher that sends String messages
#    to the 'helloworld' topic every second using a timer.
# 2. The hellopublisher method creates a String message with the content "Hello_world" and publishes it.
# 3. The main function initializes the ROS 2 Python client library, creates the publisher node, and starts spinning
#    (processing callbacks) until interrupted by the user (Ctrl+C).
# 4. The script prints status messages when starting and terminating the node.
#
# This is a basic example of a ROS 2 publisher node in Python, useful for learning ROS 2 communication patterns.