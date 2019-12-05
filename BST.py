class Node:
    def __init__(self, value=None, size=0):
        self.value = value
        self.size = size
        self.left = None
        self.right = None
        self.parent = None  # pointer to parent node in tree


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.duplicates = 0
        self.file = open('numbers.log', "w")

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            self.size += 1
            self.file = open('numbers.log', 'a')
            self.file.write('{}\n'.format(value))
            self.file.close()
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node  # set parent
                self.size += 1
                self.file = open('numbers.log', 'a')
                self.file.write('{}\n'.format(value))
                self.file.close()
            else:
                self._insert(value, cur_node.left)

        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node  # set parent
                self.size += 1
                self.file = open('numbers.log', 'a')
                self.file.write('{}\n'.format(value))
                self.file.close()
            else:
                self._insert(value, cur_node.right)
        else:
            self.duplicates += 1

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

    def size(self):
        return self.size(self.root)

    def size(x):
        if (x == None):
            return 0
        else:
            return x.size
