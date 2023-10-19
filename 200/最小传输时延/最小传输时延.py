N, M = [int(x) for x in input().split()]
graph = {}

for i in range(M):
    u,v,w = [int(x) for x in input().split()]
    if u in graph:
        graph[u][0].append(v)
        graph[u][1].append(w)
    else:
        graph[u] = [[v], [w]]


start, end = [int(x) for x in input().split()]
print(graph)

import copy

class Solution:
    def __init__(self) -> None:
        self.graph = None
        self.has_search = None
        self.start = None
        self.end = None
        self.res = float("inf")
        self.trace = []

    def dfs(self, cur, weight, path):
        if cur == self.end:
            if self.res > weight:
                self.trace = copy.deepcopy(path)
                self.res = weight
        
        if cur in self.graph:
            nodes = self.graph[cur][0]
            for i in range(len(nodes)):
                weight += self.graph[cur][1][i]
                path.append(cur)

                self.dfs(nodes[i], weight, path)

                weight -= self.graph[cur][1][i]
                path.pop()



    def solve(self, graph, N, start, end):
        self.graph = graph
        self.has_search = [0] * N
        self.start = start
        self.end = end
        self.dfs(start, 0, [])

s = Solution()
s.solve(graph, N, start, end)

print(s.res if s.res != float("inf") else -1)
print(s.trace)

'''
3 3
1 2 11
2 3 13
1 3 50
1 3

6 9
1 2 5
1 3 2
2 4 3
2 5 2
3 4 3
3 5 4
4 6 6
5 6 1
3 2 1
1 6

7 9
1 2 5
1 3 2
2 4 3
2 5 2
3 4 3
3 5 4
4 6 6
5 6 1
3 2 1
1 7
'''

