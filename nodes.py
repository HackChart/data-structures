class LinearNode:
    """Basic Node Structure"""
    def __init__(self, data=None, next_node=None):
        """Data and pointer default to none"""
        self.data = data
        self.next_node = next_node

    def set_next_node(self, new_node):
        self.next_node = new_node


class BidirectionalNode(LinearNode):
    """Basic Bidirectional Node Structure, inherits from LinearNode"""
    def __init__(self, data=None, next_node=None, prev_node=None):
        """Data and bidirectional points default to none"""
        super(BidirectionalNode, self).__init__(data, next_node)
        self.prev_node = prev_node
