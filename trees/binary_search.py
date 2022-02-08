from pprint import pformat


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        """
        Return a string of all the Nodes using in order traversal
        """
        return str(self.root)

    def is_empty(self):
        pass

    def add(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            tmp = self.root
            while True:
                if data < tmp.data:
                    if tmp.left is None:
                        tmp.left = node
                        break
                    tmp = tmp.left
                else:
                    if tmp.right is None:
                        tmp.right = node
                        break
                    tmp = tmp.right

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.data)
        self.in_order(root.right)

    def pre_order(self, root):
        if not root:
            return
        print(root.data)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data)

    def delete_node(self, value):
        if value == self.root.data:
            new_root = self.root.right
            tmp = self.root.right
            while tmp.left:
                tmp = tmp.left
            tmp.left = self.root.left
            self.root = new_root
        else:
            curr = self.root
            prev = None
            while curr is not None and curr.data != value:
                prev = curr
                if value < curr.data:
                    curr = curr.left
                else:
                    curr = curr.right

            if curr.right is None and curr.left is None:
                if prev.left == curr:
                    prev.left = None
                else:
                    prev.right = None
            elif curr.right is None and curr.left:
                prev.left = curr.left
            elif curr.left is None and curr.right:
                prev.right = curr.right
            else:
                temp = curr.right
                while temp.left:
                    temp = temp.left
                temp.left = curr.left
                prev.right = curr.right


def main():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(20)
    tree.add(30)
    tree.add(5)
    tree.add(2)
    tree.add(4)
    tree.add(15)
    tree.add(25)
    tree.add(23)
    # print(tree)
    #
    # print("delete 20")
    # tree.delete_node(20)

    print(tree)

    print("delete 25")
    tree.delete_node(25)
    print(tree)

    # print("delete 4")
    # tree.delete_node(4)
    # print(tree)

    # print("Pre order")
    # tree.pre_order(tree.root)
    # print("Post order")
    # tree.post_order(tree.root)
    # tree.add(7)
    # tree.add(50)
    # print(tree)


if __name__ == '__main__':
    main()
