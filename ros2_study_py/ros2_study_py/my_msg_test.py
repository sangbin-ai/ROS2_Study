import rclpy
from rclpy.node import Node

class MyMsgTest (Node):
    def __init__ (self):
        super().__init__('my_msg_test')
        self.count = 0.0

        self.timer = self.create_timer(
            1.0,
            self.timer_callback
        )
    def timer_callback(self):

        self.get_logger().info(f'{self.count}')
        self.count += 1.0
def main(args=None):
    rclpy.init(args=args)

    node = MyMsgTest()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    