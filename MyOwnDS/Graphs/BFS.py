"""
Typical BFS implementation using a queue
"""


def BFS(graph, start):
    # assumes an adjacency list
    visited = [start]
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


if __name__ == "__main__":

    # Expectation: ['SFO', 'ORL', 'JFK', 'LAX', 'DFW', 'LGA', 'HNL']

    plane_routes = {
        'JFK': ['SFO', 'LAX', 'LGA'],
        'SFO': ['ORL'],
        'ORL': ['JFK', 'LAX', 'DFW'],
        'LAX': ['DFW'],
        'DFW': [],
        'HNL': [],
        'LGA': ['HNL']
    }

    print(BFS(plane_routes, 'SFO'))