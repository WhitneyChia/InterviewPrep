"""
Typical DFS implementation
"""


def DFS_adj_list(graph, start):
    # assumes an adjacency list
    """ Don't have to use a stack, can just use a list and recurse """
    visited = [start]
    visited = DFS_helper(graph, start, visited)
    return visited


def DFS_helper(graph, vertex, visited):
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            visited.append(neighbour)
            visited = DFS_helper(graph, neighbour, visited)
    return visited


if __name__ == "__main__":

    # Expectation is: ['SFO', 'ORL', 'JFK', 'LGA', 'HNL', 'LAX', 'DFW']

    plane_routes = {
        'JFK': ['SFO', 'LGA'],
        'SFO': ['ORL'],
        'ORL': ['JFK', 'LAX', 'DFW'],
        'LAX': ['DFW'],
        'DFW': [],
        'HNL': [],
        'LGA': ['HNL']
    }

    print(DFS_adj_list(plane_routes, 'SFO'))
