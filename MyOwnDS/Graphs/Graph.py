"""
There are two ways to represent graphs, an adjacency list and an adjacency Matrix.
An adjacency list will take up less space, but harder to look up
An adjacency Matrix, especially if sparse will take up more space but fast lookup i.e. graph[i][j]
In an adjacency Matrix, if there is a weighted edge, that is number in the Matrix
"""


def BFS_order_for_adj_list(adj_list, source_node):
    visited = [source_node]
    queue = [source_node]

    while queue:
        node_to_eval = queue.pop()
        for neighbor in adj_list[node_to_eval]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return visited


def BFS_possible_to_reach_adj_list(adj_list, source_node, target_node):
    # Alternatively, can run BFS visited order exhaustively and just check if target in list
    visited = [source_node]
    queue = [source_node]

    while queue:
        node_to_eval = queue.pop()
        for neighbor in adj_list[node_to_eval]:
            if neighbor == target_node:
                return True
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return False


def DFS_order_for_adj_list(adj_list, source_node):
    visited = [source_node]
    visited = DFS_helper(adj_list, source_node, visited)
    return visited


def DFS_helper(adj_list, source_node, visited):
    for neighbor in adj_list[source_node]:
        if neighbor not in visited:
            visited.append(neighbor)
            visited = DFS_helper(adj_list, neighbor, visited)
    return visited


def DFS_possible_to_reach_adj_list(adj_list, source_node, target_node):
    # Just running DFS exhaustively and checking if target is in visited result
    visited = DFS_order_for_adj_list(adj_list, source_node)
    if target_node in visited:
        return True
    return False


if __name__ == "__main__":

    plane_routes_adj_list = {
        'JFK': ['SFO', 'LGA'],
        'SFO': ['ORL'],
        'ORL': ['JFK', 'LAX', 'DFW'],
        'LAX': ['DFW'],
        'DFW': [],
        'HNL': [],
        'LGA': ['HNL']
    }

    print(BFS_order_for_adj_list(plane_routes_adj_list, 'SFO'))
    print(DFS_order_for_adj_list(plane_routes_adj_list, 'SFO'))

    more_plane_routes_adj_list = {
        'JFK': ['SFO', 'LGA'],
        'SFO': ['ORL'],
        'ORL': ['JFK', 'LAX', 'DFW'],
        'LAX': ['DFW'],
        'DFW': [],
        'HNL': [],
        'LGA': ['HNL'],
        'MIA': ['ORD']
    }

    print(BFS_possible_to_reach_adj_list(more_plane_routes_adj_list, 'SFO', 'MIA'))
    print(BFS_possible_to_reach_adj_list(more_plane_routes_adj_list, 'SFO', 'LGA'))
    print(DFS_possible_to_reach_adj_list(more_plane_routes_adj_list, 'SFO', 'MIA'))
    print(DFS_possible_to_reach_adj_list(more_plane_routes_adj_list, 'SFO', 'LGA'))

    # Assuming the indices are 'JFK', 'SFO', 'ORL', 'LAX', 'DFW', 'HNL', 'LGA'
    # This will be N x N and there is no edge to itself, unless there is....
    plane_routes_adj_matrix = [
        [0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1],
    ]

    new_bills, remainder = divmod(100, 100)
    print(new_bills)
    print(remainder)