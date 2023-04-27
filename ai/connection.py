
class connection:
    def __init__(self, in_node, out_node, weight):
        self.in_node = in_node
        self.weight = weight
        self.out_node = out_node

        self.enabled = True

    def feed_forward(self):
        self.in_node.activate_node()
        self.out_node.feed(self.weight, self.in_node.activated_value)
