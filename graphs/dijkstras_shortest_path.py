# reference : https://learning.oreilly.com/videos/working-with-algorithms/9781491907818/9781491907818-video182092/
# representing adjecency list using the dictionary
# why not use just the dictionary instead of creating this abstract data type
# tomo if you need to have some state, it becomes easier

# dijkstra' algo
# ref : https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e

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

    def get_low_cost(self, known_distance, unvisited):
        return min({key: value for key, value in known_distance.items() if value and key in unvisited},
                   key=lambda k: known_distance[k][1])

    # noinspection PyTypeChecker
    def shortest_path(self, start_node):
        known_distance = dict.fromkeys(self._graph, None)
        known_distance[start_node] = (start_node, 0)
        print(known_distance)

        unvisited = list(known_distance.keys())
        visited = set()

        while len(visited) != len(known_distance):
            next_to_be_visited = self.get_low_cost(known_distance, unvisited)
            for neighbor, distance in self.neighbours(next_to_be_visited):
                if neighbor not in visited:
                    if known_distance[neighbor] is not None:
                        parent_node, known_cost = known_distance[neighbor]
                        current_cost = distance + known_distance[next_to_be_visited][1]
                        if current_cost < known_cost:
                            known_distance[neighbor] = (next_to_be_visited, current_cost)
                    else:
                        current_cost = distance + known_distance[next_to_be_visited][1]
                        known_distance[neighbor] = (next_to_be_visited, current_cost)
            visited.add(next_to_be_visited)
            unvisited.remove(next_to_be_visited)
        print(known_distance)


def main():
    # look at the graph.png in directory
    simple = {
        'a': [('b', 7), ('c', 3)],
        'b': [('a', 7), ('c', 1), ('d', 2), ('e', 6)],
        'c': [('b', 1), ('a', 3), ('d', 2)],
        'd': [('c', 2), ('b', 2), ('e', 4)],
        'e': [('d', 4), ('b', 6)],
    }

    g = Graph(simple)
    g.shortest_path('a')


if __name__ == '__main__':
    main()
