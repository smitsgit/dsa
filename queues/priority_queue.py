from heapq import heappush, heappop, heapify


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0

    def add(self, data, priority):
        # data : (value, index)
        heappush(self.heap, (-priority, self.index, data))
        self.index += 1

    def get(self):
        return heappop(self.heap)[-1]


def main():
    queue = PriorityQueue()
    queue.add(10, 4)
    queue.add(10, 4)
    queue.add(20, 6)
    print(queue.heap)


if __name__ == '__main__':
    main()
