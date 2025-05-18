# Напишите алгоритм поиска в ширину (BFS)
#
# Формат входных данных:
# Граф задаётся в виде словаря, где ключи — вершины, а значения — списки смежных вершин.
#
# Обход начинается с заданной стартовой вершины.
# Требуется:
# 1.Реализовать BFS — обход графа в ширину.
# 2.Вернуть самый коротки маршрут от точки старта до точки назначения.

# Пример входных данных
# city_map = {
#     'Home': ['Park', 'School', 'Mail'],
#     'Park': ['Home', 'Museum', 'Cafe'],
#     'School': ['Home', 'Library', 'Mail'],
#     'Mail': ['Home', 'School', 'Hospital'],
#     'Library': ['School', 'Hospital'],
#     'Hospital': ['Library', 'Mail', 'Office'],
#     'Cafe': ['Park', 'Theater', 'Office'],
#     'Museum': ['Park', 'Shop'],
#     'Shop': ['Museum', 'Theater'],
#     'Theater': ['Shop', 'Cafe'],
#     'Office': ['Cafe', 'Hospital']
# }
# start = "Home"
# finish = "Theater"
#
# Пример выходных данных
# ['Home', 'Park', 'Cafe', 'Theater']
city_map = {
     'Home': ['Park', 'School', 'Mail'],
     'Park': ['Home', 'Museum', 'Cafe'],
     'School': ['Home', 'Library', 'Mail'],
     'Mail': ['Home', 'School', 'Hospital'],
     'Library': ['School', 'Hospital'],
     'Hospital': ['Library', 'Mail', 'Office'],
     'Cafe': ['Park', 'Theater', 'Office'],
     'Museum': ['Park', 'Shop'],
     'Shop': ['Museum', 'Theater'],
     'Theater': ['Shop', 'Cafe'],
     'Office': ['Cafe', 'Hospital']}
start = 'Home'
finish = 'Cafe'
from collections import deque
def bfs(start, finish):
    queue = deque([start])
    visited = []
    while queue:
        path = queue.pop()
        to4ka = path[-1]
        if to4ka == finish:
            return path
        if to4ka not in visited:
            visited.append(to4ka)
            for i in city_map.get(to4ka, []):
                new_path = path + [i]
                queue.append(new_path)
    return None

print(bfs(start, finish))