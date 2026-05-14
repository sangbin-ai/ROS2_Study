import rclpy
from rclpy.node import Node
from my_interfaces.srv import Calculator

class MinimalService(Node):

    def __init__(self):
        super().__init__("minimal_service")
        self.srv = self.create_service(
            Calculator, "calculator", self.calculator_callback
        )

    def calculator_callback(self, request, response):
        response.add = request.a + request.b
        response.sub = request.a - request.b
        response.mul = request.a * request.b

        if request.b == 0:
            response.div = 0.0
        else:
            response.div = request.a / request.b
        self.get_logger().info(
            f"""
        a : {request.a}
        b : {request.b}

        add: {response.add}
        sub: {response.sub}
        mul: {response.mul}
        div: {response.div}
        """
        )

        return response

def main():
    rclpy.init()
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
