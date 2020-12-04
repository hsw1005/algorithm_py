# 20151594 함승우 Dijkstra's Algorithm

import sys

# 1. 간선이 없는 vertex를 INF로 처리.
INF = 999

# 2. Graph class 선언.
class Graph():

    # 3. 초기화
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # 4. 출력부.
    def printSolution(self, dist, touch):
        print("\nF -> ")
        for node in range(self.V):
            print("v1 to v{0}".format(node+1), "-> cost : ", dist[node])


    # 5. 최소 거릿 값을 계산.
    def minDistance(self, dist, sptSet):

        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # 6. 다익스트라 알고리즘 실행.
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)

            # 7. 목적지까지 최소 거리를 넣는다.
            sptSet[u] = True

            # 8. 갱신.
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

"""
# 9. 교재 데이터.
g = Graph(5)
g.graph = [
    [0, 7, 4, 6, 1],
    [7, 0, 2, 3, INF],
    [4, 2, 0, 5, INF],
    [6, 3, 5, 0, 1],
    [1, INF, INF, 1, 0]
]
"""

# 10. 자작 데이터.
g = Graph(5)
g.graph = [
    [0, 1, 8, 4, 2],
    [1, 0, INF, 2, INF],
    [8, INF, 0, 3, 3],
    [4, 2, 3, 0, INF],
    [2, INF, 3, INF, 0]
]

# 11. 실행.
g.dijkstra(0)
