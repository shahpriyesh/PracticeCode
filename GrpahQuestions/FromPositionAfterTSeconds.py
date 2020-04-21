class FrogPositionAfterTSeconds:
    def __init__(self):
        self.probability = 0

    def frogPos(self, n, edges, t, target):
        self.probability = 1
        visited = [False]*(n+1)
        visited[1] = True
        if not self.frogUtil(edges, 1, t, target, visited):
            return 0
        return self.probability

    def frogUtil(self, edges, vertice, t, target, visited):
        if vertice == target:
            return True
        if t == 0:
            return False
        nextVertices = []
        for edge in edges:
            # if edges are given in reverse order than we want than flip them
            if edge[1] < edge[0]:
                edge[0], edge[1] = edge[1], edge[0]
            # check if edge[0] matches the vertice we are looking for, than put its connection in nextVertice
            if vertice == edge[0]:
                nextVertices.append(edge[1])

        if nextVertices:
            self.probability *= (1 / len(nextVertices))

        for v in nextVertices:
            visited[v] = True
            if self.frogUtil(edges, v, t-1, target, visited):
                return True
            visited[v] = False

        return False


object = FrogPositionAfterTSeconds()
print(object.frogPos(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4))
print(object.frogPos(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1, 7))
print(object.frogPos(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6))
print(object.frogPos(3, [[2,1],[3,2]], 1, 2))