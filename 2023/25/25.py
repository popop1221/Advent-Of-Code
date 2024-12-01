import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

sys.setrecursionlimit(150000)

with open('input.txt') as f:
    real_input = f.readlines()

with open('test_input.txt') as f:
    test_input = f.readlines()

inputt = real_input
inputt = [line.replace("\n", "") for line in inputt]

graph = {}
to_test = []
G = nx.Graph()
for line in inputt:
    temp = line.split(": ")
    temp2 = temp[1].split(" ")
    for comp in temp2:
        to_test.append((temp[0], comp))

        if temp[0] not in graph:
            G.add_node(temp[0])
            graph[temp[0]] = []

        if comp not in graph:
            graph[comp] = []
            G.add_node(comp)

        graph[temp[0]].append(comp)
        graph[comp].append(temp[0])
        G.add_edge(temp[0], comp)


def evaluate(pos, marked):
    for next in graph[pos]:
        if next not in marked:
            marked.append(next)
            evaluate(next, marked)


print(graph)
nx.draw(G, with_labels=True)
plt.show()

graph["lhg"].remove("llm")
graph["llm"].remove("lhg")
graph["frl"].remove("thx")
graph["thx"].remove("frl")
graph["fvm"].remove("ccp")
graph["ccp"].remove("fvm")
G.remove_edge("llm", "lhg")
G.remove_edge("thx", "frl")
G.remove_edge("fvm", "ccp")

print(graph)
nx.draw(G, with_labels=True)
plt.show()

result = ["ccp"]
evaluate("ccp", result)
print((len(graph) - len(result)) * len(result))

"""
for test in to_test:
    graph[test[0]].remove(test[1])
    graph[test[1]].remove(test[0])
    for test2 in to_test:
        if test == test2:
            continue

        graph[test2[0]].remove(test2[1])
        graph[test2[1]].remove(test2[0])
        for test3 in to_test:
            if test == test3 or test2 == test3:
                continue
            graph[test3[0]].remove(test3[1])
            graph[test3[1]].remove(test3[0])

            marked = ["cxq"]
            evaluate("cxq", marked)
            graph[test3[0]].append(test3[1])
            graph[test3[1]].append(test3[0])
            if len(marked) != len(graph):
                print(f"{len(graph)}  {len(marked)}   {(len(graph) - len(marked)) * len(marked)}")
        graph[test2[0]].append(test2[1])
        graph[test2[1]].append(test2[0])
    graph[test[0]].append(test[1])
    graph[test[1]].append(test[0])
"""
