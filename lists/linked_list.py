class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def __iter__(self):
        tmp = self.head
        while tmp:
            yield tmp.data
            tmp = tmp.next

    def __len__(self):
        return self.count

    def delete_head(self):
        self.delete_nth(0)

    def delete_tail(self):
        self.delete_nth(len(self) - 1)

    def delete_nth(self, index=0):
        if not 0 <= index < len(self):
            raise IndexError("Out of range")

        if index == 0:
            self.head = self.head.next
        else:
            tmp = self.head
            for _ in range(index - 1):
                tmp = tmp.next

            delete_node = tmp.next
            tmp.next = delete_node.next

    def insert_nth(self, value, index):
        if not 0 <= index <= len(self):
            raise IndexError("Out of range")

        node = Node(value)

        if not self.head:
            self.head = node
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            tmp = self.head
            for _ in range(index - 1):
                tmp = tmp.next

            node.next = tmp.next
            tmp.next = node
        self.count += 1

    def insert_tail(self, value):
        self.insert_nth(value, len(self))

    def insert_head(self, value):
        self.insert_nth(value, 0)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def __repr__(self):
        return f"{list(self)}"

    def is_empty(self):
        return self.head is None


def main():
    lst = LinkedList()
    lst.insert_head(10)
    lst.insert_head(20)
    lst.insert_tail(30)
    lst.insert_head(40)
    print(lst)
    lst.delete_head()
    print(lst)
    lst.reverse()
    print(lst)


if __name__ == '__main__':
    main()
