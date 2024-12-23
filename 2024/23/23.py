import sys
import networkx as nx
import matplotlib.pyplot as plt

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

links = {}
for line in inputt:
    sp = line.split("-")
    if sp[0] not in links:
        links[sp[0]] = []
    if sp[1] not in links:
        links[sp[1]] = []
    links[sp[0]].append(sp[1])
    links[sp[1]].append(sp[0])

networks = []
for comp1 in links:
    for comp2 in links:
        for comp3 in links:
            if comp2 in links[comp1] and comp3 in links[comp1] and comp3 in links[comp2] and {comp1, comp2, comp3} not in networks:
                networks.append({comp1, comp2, comp3})
print(networks)
print(len(networks))

result = 0
for network in networks:
    for elem in network:
        if elem.startswith("t"):
            result += 1
            break

print(result)

print("----- PART 2 -----")

G = nx.Graph()
for node in links:
    G.add_node(node)
for node in links:
    for node2 in links[node]:
        G.add_edge(node, node2)
        G.add_edge(node2, node)
nx.draw(G, with_labels=True)
plt.show()

temp = list(nx.find_cliques(G))
result = temp[0]
for t in temp:
    if len(t) > len(result):
        result = t
print(sorted(result))
