with open('input.txt') as f:
    lines = f.readlines()

with open('test_inputs') as f:
    test_input = f.readlines()

graph_temp = {}
nodes = set()
valve_node = set()
values = {}
for line in lines:
#for line in test_input:
    line = line.replace("\n", "")
    temp = line.split(" ")
    name = temp[1]
    rate = int(temp[4].split("=")[1].replace(";", ""))
    nei = [ne.replace(",", "") for ne in temp[9:]]
    nodes.add(name)
    values[name] = rate
    graph_temp[name] = nei
    if rate != 0:
        valve_node.add(name)

print(graph_temp)
print(values)


def shortest_path(start, end):
    path_list = [[start]]
    path_index = 0
    previous_nodes = {start}
    if start == end:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph_temp[last_node]
        if end in next_nodes:
            current_path.append(end)
            return current_path

        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(next_node)
        path_index += 1
    return []


graph = {}
for node in nodes:
    dists = {}
    if values[node] == 0 and node != "AA":
        continue
    for node1 in nodes:
        if node != node1 and values[node1] != 0:
            dists[node1] = len(shortest_path(node, node1)) - 1
    graph[node] = dists
print(graph)


def get_pression(opened):
    result = 0
    for valve in opened:
        result += values[valve]
    return result


all_valves = [2 if values[name] != 0 else 1 for name in graph.keys()].count(2)
memo = {}
itter = 0


def simulate(node_start, opened, minute, result, acc):
    global itter
    itter += 1
    if minute == 30:
        return result, acc

    if memo.keys().__contains__((node_start, frozenset(opened), minute, result)):
        return memo[(node_start, frozenset(opened), minute, result)]

    if all_valves == len(opened):
        return result + (30 - minute) * get_pression(opened), acc + [f"{(30-minute)}  * {get_pression(opened)}"]

    options = []

    if node_start not in opened and values[node_start] != 0:
        new_opened = opened.copy()
        new_opened.append(node_start)
        options.append(simulate(node_start, new_opened, minute + 1, result + get_pression(opened), acc + [f"Open {node_start}"]))

    for nei in graph[node_start]:
        if graph[node_start][nei] + minute < 30 and nei not in opened:
            options.append(simulate(nei, opened, minute + graph[node_start][nei], result + get_pression(opened) * graph[node_start][nei], acc + [f"Voy to {nei}"]))

    if not options:
        return 0, []

    memo[(node_start, frozenset(opened), minute, result)] = max(options)
    return max(options)[0], max(options)[1]

print(simulate("AA", [], 0, 0, []))
print(itter)

print("----- PART 2 -----")
memo = {}
itter = 0


def simulate_2(node_start, opened, minute, eleph):
    if minute == 26:
        if eleph:
            return 0
        return simulate_2("AA", opened, 0, True)

    global itter
    itter += 1

    if memo.keys().__contains__((node_start, frozenset(opened), minute, eleph)):
        return memo[(node_start, frozenset(opened), minute, eleph)]

    if all_valves == len(opened):
        return 0

    options = []
    if node_start != "AA" and not eleph:
        options.append(simulate_2("AA", opened, 0, True))

    if node_start not in opened and values[node_start] != 0:
        new_opened = opened.copy()
        new_opened.append(node_start)
        options.append(values[node_start] * (25 - minute) + simulate_2(node_start, new_opened, minute + 1, eleph))

    for nei in graph[node_start]:
        if graph[node_start][nei] + minute < 26 and nei not in opened:
            options.append(simulate_2(nei, opened, minute + graph[node_start][nei], eleph))

    if not options:
        return 0

    memo[(node_start, frozenset(opened), minute, eleph)] = max(options)
    return max(options)

print(simulate_2("AA", [], 0, False))
print(itter)
