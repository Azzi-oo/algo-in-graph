# Чтение графа из файла
with open("graph.txt", "r") as f:
    edges = [tuple(map(int, line.strip().split())) for line in f]
print(edges)

# Подсчет степеней вершин
degrees = [0] * (max(max(edges))+1)
for edge in edges:
    degrees[edge[0]] += 1
    degrees[edge[1]] += 1

# Нахождение вершины с максимальной степенью
max_degree = max(degrees)
max_vertex = degrees.index(max_degree)

# Вывод результата
print(f"Вершина с максимальной степенью: {max_vertex}")
