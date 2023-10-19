# 深度优先搜索

N = int(input())
graph = {} # {a:b}, [a, b], b依赖a， a-->b
while True:
    try:
        line = input()
        if not line:
            break
        a, b = [int(x) for x in line.split()]
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
    except:
        break


class Solution:
    def __init__(self, graph, N):
        self.has_loop = False
        self.graph = graph
        self.visited = [0] * N # 0,1,2分别表示未被搜索、正在被搜索、搜索完成
        self.path = [] # 存储拓扑排序
        self.N = N

    def dfs(self, node):
        if self.has_loop: # 有环全部退出
            return

        # 取出当前节点指向的其他节点
        if node in self.graph:
            self.visited[node] = 1 # 标记该节点正在被搜索
            for item in self.graph[node]:   
                if self.visited[item] == 1 : # 当前指向的其他节点之前已被遍历，说明图中存在环，直接退出
                    self.has_loop = True
                    return
                elif self.visited[item] == 0: # 当前指向的其他节点之前未被遍历，则继续搜索指向的节点
                    self.dfs(item)
        '''
        这里使用2标记某一节点已被完全搜索完，可以避免当出现
            1   2
        3
                    4
            6   0   
                    5
        这个例子，先搜索0，0搜索完后搜索1,2,3,4,5,6,但是当搜索3和6时， 0又被搜索了一遍，造成重复
        不标记本题也可求解，但无法进行拓扑排序且会大大增加复杂度
        '''
        self.visited[node] = 2 
        self.path.append(node)


    def solve(self):
        for i in range(self.N): # 搜索每一个节点
            if not self.has_loop and not self.visited[i]:
                self.dfs(i)
        print(self.path[::-1]) # 由于入队时在后面的先入队（最先入队的是没有出度的节点),因而拓扑排序需反序
        return not self.has_loop
    

    
print(graph)

s = Solution(graph, N)
res = s.solve()
print(res)


