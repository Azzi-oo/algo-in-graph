# Чтение графа из файла
with open("graph2.txt", "r") as f:
    edges = [tuple(map(int, line.strip().split())) for line in f]

# Создание списка смежности
adj_list = {}
for edge in edges:
    if edge[0] not in adj_list:
        adj_list[edge[0]] = []
    if edge[1] not in adj_list:
        adj_list[edge[1]] = []
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])

# Функция поиска в ширину
def bfs(graph, start):
    visited = [False] * (max(graph)+1)
    queue = [start]
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

# Вызов функции поиска в ширину
start_vertex = 1
print("Обход в ширину начиная с вершины", start_vertex)
bfs(adj_list, start_vertex)