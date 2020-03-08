inf = 9999999999
graph = {'Oradea': {'Zerind': 71, 'Sibiu': 151},
         'Zerind': {'Oradea': 71, 'Arad': 75},
         'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
         'Timisoara': {'Arad': 118, 'Lugoj': 111},
         'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
         'Mehadia': {'Lugoj': 70, 'Dobreta': 70},
         'Dobreta': {'Mehadia': 75, 'Craiova': 120},
         'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
         'Sibiu': {'Arad': 140, 'Oradea': 151, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
         'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
         'Fagaras': {'Sibiu': 99, 'Bucharest': 221},
         'Pitesti': {'Bucharest': 101, 'Rimnicu Vilcea': 97, 'Craiova': 138},
         'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
         'Giurgiu': {'Bucharest': 90},
         'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
         'Hirsova': {'Urziceni': 98, 'Eforie': 86},
         'Eforie': {'Hirsova': 86},
         'Vaslui': {'Urziceni': 142, 'Iasi': 92},
         'Iasi': {'Neamt': 87, 'Vaslui': 92},
         'Neamt': {'Iasi': 87}}

dist = {'Arad': inf, 'Bucharest': inf, 'Craiova': inf, 'Dobreta': inf, 'Eforie': inf, 'Fagaras': inf, 'Giurgiu': inf,
        'Hirsova': inf, 'Iasi': inf, 'Lugoj': inf, 'Mehadia': inf, 'Neamt': inf, 'Oradea': inf, 'Pitesti': inf,
        'Rimnicu Vilcea': inf, 'Sibiu': inf, 'Timisoara': inf, 'Urziceni': inf, 'Vaslui': inf, 'Zerind': inf}

source = 'Arad'
dest = 'Bucharest'

queue = []
queue.append((0, source))
dist[source] = 0

while queue:
    u = queue[0]
    queue.remove(u)
    for v in graph[u[1]].keys():
        if (graph[u[1]][v] + u[0]) < dist[v]:
            dist[v] = graph[u[1]][v] + u[0]
            queue.append((dist[v], v))

if dist[dest] == inf:
    print("Not Found\n")
else:
    print('Found!\nDist: ')
    print(dist[dest])
