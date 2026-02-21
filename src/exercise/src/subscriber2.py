import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class hellosubscriber(Node):
    def __init__(self):
        super().__init__("helloworldpub")
        self.sub= self.create_subscription(String,"helloworld",self.subscriber_callback,10)
        
    def subscriber_callback(self,msg):
        print("recived "+ msg.data)
        
        






def main(args=None):
    rclpy.init(args=args)
    my_sub=hellosubscriber()
    rclpy.spin(my_sub)






if __name__=="__main__":
    main()

# ----------------------
# Code Explanation:
# This script is a simple ROS 2 subscriber node using rclpy (the ROS 2 Python client library).
#
# 1. Imports:
#    - rclpy: Core ROS 2 Python library.
#    - Node: Base class for all ROS 2 nodes.
#    - String: Standard message type for string data.
#
# 2. Class hellosubscriber(Node):
#    - Inherits from Node.
#    - Initializes the node with the name "helloworldpub".
#    - Creates a subscription to the topic "helloworld" with message type String.
#    - The callback function 'subscriber_callback' is called whenever a message is received on this topic.
#    - The callback prints the received message data to the console.
#
# 3. main():
#    - Initializes the ROS 2 Python client library.
#    - Instantiates the hellosubscriber node.
#    - Spins the node, allowing it to process incoming messages until the program is stopped.
#
# 4. Entry Point:
#    - If the script is run directly, it calls main().
#
# Note: The node name "helloworldpub" is a bit misleading since this is a subscriber. It might be better to name it "helloworldsub" or something similar for clarity.
# Note: There are some minor typos (e.g., class name should be capitalized by convention, and node name might be better as 'helloworldsub'), but the code will function as a basic ROS 2 subscriber.