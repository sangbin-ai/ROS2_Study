import rclpy
from rclpy.node import Node
from my_interfaces.srv import Calculator

import sys

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__("minimal_client_async")
        self.cli = self.create_client(Calculator, "calculator")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("service not available, waiting again...")
        self.req = Calculator.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)


def main():
    rclpy.init()
    minimal_client = MinimalClientAsync()
    
    future = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(minimal_client, future)
    response = future.result()
    minimal_client.get_logger().info(
        f"""
        a : {sys.argv[1]}
        b : {sys.argv[2]}

        add: {response.add}
        sub: {response.sub}
        mul: {response.mul}
        div: {response.div}
        """
        )


    minimal_client.destroy_node()
    rclpy.shutdown()
