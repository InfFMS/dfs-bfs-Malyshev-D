# Реализовать алгоритм Кана для топологической сортировки
# Пример с пошаговой работой алгоритма
# Граф: A → B → C
#       A → D
graph = {'A': ['B', 'D', 'E'],
         'B': ['C'],
         'C': [],
         'D': [],
         'E': ['D']}


# Шаги:
# 1. Начальные вершины без входящих рёбер: [A]
# 2. Обрабатываем A → результат [A], обновляем степени B(1→0), D(1→0)
# 3. Вершины для обработки: [B, D]
# 4. Обрабатываем B → результат [A,B], обновляем степень C(1→0)
# 5. Обрабатываем D → результат [A,B,D]
# 6. Обрабатываем C → результат [A,B,D,C]
# 7. Все вершины обработаны → сортировка завершена
checked = []
count = {}
def kan(a):
        if a not in checked:
                checked.append(a)
                for i in graph[a]:
                        ind = graph[a].index(i)
                        count[graph[a][ind]] -= 1
                        count[a] = -1
                        kan(i)


for i in graph:
        for j in graph:
                if i not in count:
                     count[i] = 0
                if i in graph[j]:
                        count[i] += 1
while len(checked) < len(graph):
        for m in count:
                if count[m] == 0:
                        start = m
                        break
        kan(start)

print(checked)