import networkx as nx


def count_paths(graph: nx.DiGraph, source, destination):
    path_count = {rack: 0 for rack in graph.nodes}
    path_count[source] = 1
    for rack in nx.topological_sort(graph):
        if rack == destination:
            break
        if path_count[rack] > 0:
            for suc in graph.successors(rack):
                path_count[suc] += path_count[rack]
    return path_count[destination]


with open("day11/input.txt", "r") as f:
    data = f.read().strip().split("\n")

connections = {(rs := row.split())[0].replace(":", ""): rs[1:] for row in data}
connections["out"] = []
G = nx.DiGraph(connections)

# Part 1
print(count_paths(G, "you", "out"))

# Part 2
assert nx.is_directed_acyclic_graph(G) and ("fft" not in nx.descendants(G, "dac"))
print(
    count_paths(G, "svr", "fft")
    * count_paths(G, "fft", "dac")
    * count_paths(G, "dac", "out")
)
