import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Припустимо, що моделюємо транспортну мережу малого міста
stations = ["Станція 1", "Станція 2", "Станція 3", "Станція 4", "Станція 5", "Станція 6"]
routes = [("Станція 1", "Станція 2"), ("Станція 2", "Станція 3"), ("Станція 3", "Станція 4"),
          ("Станція 4", "Станція 5"), ("Станція 5", "Станція 6"), ("Станція 6", "Станція 1"),
          ("Станція 1", "Станція 4"), ("Станція 2", "Станція 5"), ("Станція 3", "Станція 6")]

# Додаємо вузли та ребра в граф
G.add_nodes_from(stations)
G.add_edges_from(routes)

# Візуалізація графа
plt.figure(figsize=(8, 8))
pos = nx.circular_layout(G)  # Розміщення вузлів у вигляді кола
nx.draw_networkx(G, pos, node_color='lightblue', with_labels=True, node_size=2000, font_size=9, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = G.degree()

(num_nodes, num_edges, list(degrees))



# Завдання 2

# Створення дерева DFS та BFS для пошуку шляху між Станція 1 і Станція 5
dfs_tree = nx.dfs_tree(G, source="Станція 1")
bfs_tree = nx.bfs_tree(G, source="Станція 1")

# Визначення шляху між Станція 1 і Станція 5 у кожному з дерев
dfs_path = nx.shortest_path(dfs_tree, source="Станція 1", target="Станція 5")
bfs_path = nx.shortest_path(bfs_tree, source="Станція 1", target="Станція 5")

print(dfs_path)
print(bfs_path)

# Завдання 3

if 'WG' not in globals():
    WG = nx.Graph()
    # Додавання вершин і ребер з вагами
    WG.add_edge("Станція 1", "Станція 2", weight=3)
    WG.add_edge("Станція 2", "Станція 3", weight=2)
    WG.add_edge("Станція 3", "Станція 4", weight=4)
    WG.add_edge("Станція 4", "Станція 5", weight=1)
    WG.add_edge("Станція 5", "Станція 6", weight=3)
    WG.add_edge("Станція 6", "Станція 1", weight=7)
    WG.add_edge("Станція 1", "Станція 4", weight=5)
    WG.add_edge("Станція 2", "Станція 5", weight=6)
    WG.add_edge("Станція 3", "Станція 6", weight=2)

# Використання алгоритму Дейкстри для знаходження найкоротших шляхів з кожної станції до кожної іншої
all_pairs_dijkstra_path = dict(nx.all_pairs_dijkstra_path(WG, weight='weight'))
all_pairs_dijkstra_path_length = dict(nx.all_pairs_dijkstra_path_length(WG, weight='weight'))

print(all_pairs_dijkstra_path)
print(all_pairs_dijkstra_path_length)
