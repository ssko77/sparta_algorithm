class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
node.next = Node(4)

print(node.next.data)

