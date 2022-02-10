# reference : https://learning.oreilly.com/videos/working-with-algorithms/9781491907818/9781491907818-video182092/
# representing adjecency list using the dictionary
# why not use just the dictionary instead of creating this abstract data type
# tomo if you need to have some state, it becomes easier

from collections import defaultdict

"""
simple = {
        'a': ['c', 'g', 'b'],
        'b': ['d', 'e'],
        'c': ['d'],
        'd': ['f'],
        'g': ['c'],
        'f': ['g']
    }
"""


class Node:
    def __init__(self, value, neighbours=None):
        self._value = value
        if neighbours is None:
            self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def add_child(self, node):
        self._children.append(node)

    def neighbours(self):
        return self._children

    def depth_first(self, visited=None):
        if visited is None:
            visited = set()
        if self._value not in visited:
            yield self
        visited.add(self._value)
        for neighbor in self:
            if neighbor._value not in visited:
                yield from neighbor.depth_first(visited)


class Graph:
    def __init__(self, data: dict):
        self._graph = defaultdict(list)
        for item in data:
            new_node = Node(item)
            self._graph[item] = new_node

        for item, neighbors in data.items():
            for n in neighbors:
                self._graph[item].add_child(self._graph[n])


def main():
    # look at the graph.png in directory
    simple = {
        'a': ['c', 'g', 'b'],
        'b': ['d', 'e'],
        'c': ['d'],
        'd': ['f', 'e'],
        'g': ['c'],
        'f': ['g'],
        'e': []
    }

    g = Graph(simple)
    node = g._graph['a']
    for index, item in enumerate(node.depth_first()):
        print(item)


if __name__ == '__main__':
    main()
