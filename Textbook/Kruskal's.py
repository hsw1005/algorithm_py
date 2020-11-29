# 20151594 함승우 Kruskal's Algorithm

# 1. graph class 생성.
class Graph:

    # 2. 초기화
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # 3. u, v노드와 w edge를 더한다.
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # 4. 부모 노드를 찾는 함수.
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # 5. 부모 노드와 자식 노드를 합치는 함수.
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)


        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    # 6. kruskal minimum spanning tree.
    def KruskalMST(self):

        result = []
        i = 0
        e = 0

        # 7. graph를 w값, 즉, item[2] == ([u, v, w])을 기준으로 정렬한다.
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # 9. node의 수에서 -1만큼 (edge 수만큼)
        while e < self.V - 1:

            # 가장 작은 cost를 선택.
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # 10. cycle을 확인. cycle이 발생하지 않으면 추가.
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("\nF -> ")
        for u, v, weight in result:
            minimumCost += weight
            print("%d[node]  -- %d[node] ==> %d[cost]" % (u+1, v+1, weight))
        print("\nMST는 -> ", minimumCost)


# 11. 교재 데이터 입력
#g = Graph(5)
#g.addEdge(0, 1, 1)
#g.addEdge(0, 2, 3)
#g.addEdge(1, 2, 3)
#g.addEdge(1, 3, 6)
#g.addEdge(2, 3, 4)
#g.addEdge(2, 4, 2)
#g.addEdge(3, 4, 5)

# 12. 자작 데이터 입력
g = Graph(5)
g.addEdge(2, 3, 1)
g.addEdge(0, 1, 2)
g.addEdge(3, 4, 2)
g.addEdge(1, 3, 3)
g.addEdge(0, 2, 4)
g.addEdge(2, 4, 5)
g.addEdge(1, 3, 5)

# 13. 함수 실행.
g.KruskalMST()
