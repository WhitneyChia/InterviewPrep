"""
Problem is stated, given a bunch of FX rates, find out if there is an arbitrage opportunity.
The idea here is model it as a graph, currencies as nodes, FX rate as edges
"""

from math import log


def arbitrage(table):
    # One property of logarithms is that log(a x b) = log(a) + log(b)
    # Therefor we take the log of each exchange rate and negate to ensure positivity
    transformed_graph = [[-log(FX) for currency, FX in table[row].items()] for row in table]

    # Pick any source vertex, Bellman-Ford can run from any vertex and be correct.

    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')] * n

    min_dist[source] = 0

    # Relax edges [V -1] times, Bellman-Ford requires V - 1 iterations.
    # It is possible to be done before V - 1, if the results from one iteration to the next don't change
    # But assume V - 1

    for i in range(n - 1):
        for v in range(n):
            for w in range(n - 1):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    # If we can still relax edges after V - 1 iterations, then we have a negative cycle
    # This is the drawback of Bellman-Ford, it can't handle negative cycles
    # In our case, this is an advantage though, as it identifies arbitrage opportunities
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False


if __name__ == "__main__":

    currency_rates = {
        'USD': {'GBP': 0.77, 'INR': 71.71, 'EUR': 0.87},
        'GBP': {'USD': 1.30, 'INR': 93.55, 'EUR': 1.14},
        'INR': {'USD': 0.014, 'GBP': 0.011, 'EUR': 0.012},
        'EUR': {'USD': 1.14, 'GBP': 0.88, 'INR': 81.95}
    }

    print(arbitrage(currency_rates))
