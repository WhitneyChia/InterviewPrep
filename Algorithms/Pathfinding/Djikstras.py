import heapq


class Network:

    def __init__(self, N, edges):
        self.vertices = range(N + 1)
        self.edges = edges

    def make_graph(self):
        graph = {v: [] for v in self.vertices}

        for u, v, w in self.edges:
            graph[u].append((v, w))

        return graph


def propogate_slower(network):
    graph = network.make_graph()
    times = {node: float('inf') for node in graph}
    times[0] = 0

    q = list(graph)
    while q:
        u = min(q, key=lambda x: times[x])
        q.remove(u)
        for v, time in graph[u]:
            times[v] = min(times[v], times[u] + time)

    return max(times.values())


def propogate_better(network):
    graph = network.make_graph()
    times = {}

    q = [(0, 0)]

    while q:
        u, node = heapq.heappop(q)
        if node not in times:
            times[node] = u
            for neighbor, v in graph[node]:
                if neighbor not in times:
                    heapq.heappush(q, (u + v, neighbor))
    return max(times.values())


if __name__ == "__main__":

    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (0, 5, 4),
        (1, 3, 8),
        (2, 3, 1),
        (3, 5, 10),
        (3, 4, 5)
    ]

    network = Network(5, edges)
    print(propogate_slower(network))

    print(propogate_better(network))
