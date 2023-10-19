from collections import deque

# 广度优先搜索

N = int(input())
graph = {} # {a:b}, [a, b], b依赖a， a-->b
indegree = [0] * N # 统计节点入度
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
        indegree[b] += 1
    except:
        break

def solve(graph, indegree, N):
    # 入度为0的节点入队
    zero_indegree = deque()
    for i in range(N):
        if indegree[i] == 0:
            zero_indegree.append(i)

    path = []
    while zero_indegree:
        node = zero_indegree.popleft()
        # 入度为0的节点及其边从图中去除时，其指向的节点入度减1，在这个过程中将减1后入度为0的节点加入队列继续搜索
        if node in graph:
            for item in graph[node]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    zero_indegree.append(item)
        path.append(node) # 节点被去除后加入拓扑排序队列
    print(path)
    if len(path) == N: # 若拓扑排序队列中元素长度与图相等说明存在拓扑排序，即有向图无环
        return True
    return False

print(solve(graph, indegree, N))