class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = w

    def dijkstra(self, start):
        import heapq
        queue = [(0, start)]  # (distance, vertex)
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

    def optimize_route(self, start, end):
        distances = self.dijkstra(start)
        return distances[end] if distances[end] != float('infinity') else None
