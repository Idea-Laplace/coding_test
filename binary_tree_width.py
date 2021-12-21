import random
class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('Key %s already exists.' % key)

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count




class BinSearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            n_Children = node.countChildren()
            if n_Children == 0:
                if parent:
                    if parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None
            elif n_Children == 1:
                if node.left:
                    successor = node.left
                else:
                    successor = node.right
                if parent:
                    if parent.left == node:
                        parent.left = successor
                    else:
                        parent.right = successor
                else:
                    self.root = successor
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.key = successor.key
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

            return True

        else:
            return False

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


test = BinSearchTree()
test_list = [[random.randrange(1, 100000), f"{i}"] for i in range(1, 20)]
for idx in range(len(test_list)):
    test.insert(test_list[idx][0], test_list[idx][1])
result = test.remove()