# reference : https://learning.oreilly.com/videos/working-with-algorithms/9781491907818/9781491907818-video182092/
# representing adjecency list using the dictionary
# why not use just the dictionary instead of creating this abstract data type
# tomo if you need to have some state, it becomes easier

from collections import defaultdict

"""
{
  node1: [node2, node3],
  node2: [node1, node4],
  node3: [node1, node4]
  node4: [node2, node3]
} 
"""


class Graph:
    def __init__(self, data: dict):
        self._graph = defaultdict(list)
        self._graph |= data

    def neighbours(self, node):
        return self._graph[node]

    def add_edge(self, from_, to):
        self._graph[from_].append(to)

    def is_edge(self, from_, to):
        return to in self._graph[from_]

    def depth_first_recursive(self, start_node, visited=None):
        if not visited:
            visited = set()
        visited.add(start_node)
        print(start_node, end=' ')

        for neighbor in self.neighbours(start_node):
            if neighbor not in visited:
                self.depth_first_recursive(neighbor, visited)

    def depth_first(self, start_node):
        stack = []
        visited = set()
        stack.append(start_node)

        while stack:
            next_node = stack.pop()

            # stack can contain duplicate nodes but we print it only once
            # ex: take a look at node 'g' in the debug log
            if next_node not in visited:
                print(next_node, end=' ')
                visited.add(next_node)
            for neighbor in self.neighbours(next_node):
                if neighbor not in visited:
                    stack.append(neighbor)
            print(stack)

    def depth_util(self, stack=None, visited=None):
        for neighbor in self.neighbours(stack[-1]):
            if neighbor in stack:
                print("Cycle present", neighbor)
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                print(neighbor, stack, sep=' ')
                self.depth_util(stack, visited)
        stack.pop()

    def depth_first_recursive_stack(self, start_node, stack=None):
        # this implmentation is based on
        # https://www.youtube.com/watch?v=vf-cxgUXcMk&list=PLdo5W4Nhv31bbKJzrsKfMpo_grxuLl8LU&index=81
        # keep adding elements to stack and print them
        # pop from the stack when no unvisted neighbors are found
        # stack automatically shrinks
        if not stack:
            stack = [start_node]
            visited = set()
            visited.add(start_node)
            print(start_node, stack, sep=' ')

        self.depth_util(stack, visited)

    def bread_first(self, start_node):
        queue = []
        visited = set()

        queue.append(start_node)
        visited.add(start_node)

        while queue:
            next_node = queue.pop(0)
            print(next_node, end=' ')
            print(f"  visited: {visited}", f"neighbours: {self.neighbours(next_node)}")
            for neighbor in self.neighbours(next_node):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
            print(f"    queue: {queue}")


def main():
    # look at the graph.png in directory
    simple = {
        'a': ['c', 'g', 'b'],
        'b': ['d', 'e'],
        'c': ['d'],
        'd': ['f'],
        'g': ['c'],
        'f': ['g']
    }

    g = Graph(simple)
    g.depth_first_recursive_stack('a')
    # g.bread_first('a')
    # for item in range(5):
    #     data = next(g.depth_first_generator('a'))
    #     print(data)


if __name__ == '__main__':
    main()
