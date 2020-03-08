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


vis = {'Arad': 0, 'Bucharest': 0, 'Craiova': 0, 'Dobreta': 0, 'Eforie': 0, 'Fagaras': 0, 'Giurgiu': 0, 'Hirsova': 0,
     'Iasi': 0, 'Lugoj': 0, 'Mehadia': 0, 'Neamt': 0, 'Oradea': 0, 'Pitesti': 0, 'Rimnicu Vilcea': 0, 'Sibiu': 0,
     'Timisoara': 0, 'Urziceni': 0, 'Vaslui': 0, 'Zerind': 0}

source = 'Arad'
dest = 'Bucharest'

def dfs(u):
    if vis[u] == 1:
        return
    vis[u] = 1
    for v in graph[u].keys():
        if vis[v] == 0:
            dfs(v)

dfs(source)
if vis[dest] == 0:
    print('Not Found\n')
else:
    print('Found\n')