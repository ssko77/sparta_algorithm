class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first_node = Node(5)
second_node = Node(12)
first_node.next = second_node

print(first_node.data, first_node.next)