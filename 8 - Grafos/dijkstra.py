import heapq


def dijkstra(graph, start):
  min_heap = [(0, start)] # [(0, 'A')]
  distances = {node: float('inf') for node in graph}
  distances[start] = 0

  while min_heap:
      current_distance, current_node = heapq.heappop(min_heap)

      if current_distance > distances[current_node]:
         continue

      for neighbor, weight in graph[current_node].items():
         distance = current_distance + weight

         if distance < distances[neighbor]:
          distances[neighbor] = distance
          heapq.heappush(min_heap, (distance, neighbor))

  return distances

graph = {
  'A': {'B': 1, 'C': 4},
  'B': {'A': 1, 'C': 2, 'D': 5},
  'C': {'A': 4, 'B': 2, 'D': 1},
  'D': {'B': 5, 'C': 1}
}


shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)

# outupt / retorno esperado: {"A": 0, "B": 1, "C": 3, "D": 4}