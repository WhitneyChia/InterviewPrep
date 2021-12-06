"""
Commonly, we will be given just a list of edges.
We want to transform this into an adjacency matrix or adjacency list for our algorithms.
"""


def transform_edges_into_adj_list(num_nodes: int, edges: list):
    """
    You technically can't derive this just from edges, you must be given the number of nodes
    i.e. I have 4 nodes, no edges, I need empty lists for adjacencies for all 4
    Could use defaultdict with empty list value, but I am explicitly creating it
    """
    adj_list = {}
    for vertex in range(num_nodes):
        if vertex not in adj_list:
            adj_list[vertex] = []
    for (source, dest) in edges:
        adj_list[source].append(dest)
        adj_list[dest].append(source)
    return adj_list


def transform_edges_into_adj_matrix(num_nodes, edges: list):
    # make an empty adjacency matrix of all 0s
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    # populate the list for each edge
    for source, dest in edges:
        adjacency_matrix[source][dest] = 1
        adjacency_matrix[dest][source] = 1
    return adjacency_matrix


def get_number_components_from_edges(num_nodes: int, edges: list, use_adj_matrix=True) -> int:
    """
    Two ways to do this, from an adj matrix or an adj list.
    We'll default the action of this to an adj_matrix
    """
    if use_adj_matrix:
        adj_matrix = transform_edges_into_adj_matrix(num_nodes, edges)
        components = get_number_components_from_adj_matrix( adj_matrix)
    else:
        adj_list = transform_edges_into_adj_list(num_nodes, edges)
        components = get_number_components_from_adj_list(adj_list)
    return components


def get_number_components_from_adj_matrix(adj_matrix: list) -> int:
    """
    assumes the adjacency matrix is complete
    i.e. a row and column for every node
    """
    # get unique list of vertices
    num_nodes = len(adj_matrix)

    # Initialize components at 0
    components = 0

    # Track the vertices that we've visited already
    visited_vertices = [False for i in range(num_nodes)]

    # dfs implementation
    def dfs(vertex_idx):
        visited_vertices[vertex_idx] = True
        for dest_idx in range(len(adj_matrix[vertex_idx])):
            if not visited_vertices[dest_idx] and adj_matrix[vertex_idx][dest_idx]:
                dfs(dest_idx)

    # Iterate through the vertices, the first vertex and its dfs is one component
    # Every other source that hasn't been visited already prior is a new component
    for vertex_idx in range(num_nodes):
        if not visited_vertices[vertex_idx]:
            dfs(vertex_idx)
            components += 1

    return components


def get_number_components_from_adj_list(adj_list: dict) -> int:
    """
    assumes the adjacency list is complete
    i.e. for nodes with no edges node: []
    """
    # Initialize components at 0
    components = 0

    # Track the vertices that we've visited already
    visited_vertices = set()

    # dfs implementation
    def dfs(source_vertex_idx):
        for child_node in adj_list[source_vertex_idx]:
            if child_node not in visited_vertices:
                visited_vertices.add(child_node)
                dfs(child_node)

    for vertex_idx, dest_vertex_indices in adj_list.items():
        if vertex_idx not in visited_vertices and not dest_vertex_indices:
            # This vertex is on its own
            components += 1
        if vertex_idx not in visited_vertices:
            for dest_vertex_idx in dest_vertex_indices:
                if dest_vertex_idx not in visited_vertices:
                    dfs(dest_vertex_idx)
                    components += 1

    return components


if __name__ == "__main__":

    edges = [[0, 1], [0, 2], [2, 3], [2, 5], [4, 6], [7, 8]]
    print("Given edges: ")
    print(edges)
    print("\n")
    print("Expressed as an adjacency list: ")
    print(transform_edges_into_adj_list(9, edges))
    print("\n")
    print("Expressed as an adjacency matrix: ")
    print(transform_edges_into_adj_matrix(9, edges))

    print("\n")
    print("Let's have a scenario where we want to find the number of components of the graph")
    print("We can decide if it's easier to use an adj matrix or an adj list depending on how sparse")
    print("Using the original list of edges, we expect and answer of 3")
    print("\n")
    print("Implementation using an adj_matrix")
    print(get_number_components_from_edges(9, edges))
    print("\n")
    print("Implementation using an adj_list")
    print(get_number_components_from_edges(9, edges, use_adj_matrix=False))

    print("\n")
    print("Here is an example where the edges don't cover all nodes in the graph, I have node 0 on its own")
    print("Using the list of edges, we expect and answer of 2, everything connected is 1, and then 0 on its own")
    nodes = 4
    edges = [[2, 3], [1, 2], [1, 3]]
    print("\n")
    print("Implementation using an adj_matrix")
    print(get_number_components_from_edges(4, edges))
    print("\n")
    print("Implementation using an adj_list")
    print(get_number_components_from_edges(4, edges, use_adj_matrix=False))

