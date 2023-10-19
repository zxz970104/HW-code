# 输入获取
import sys
 
n, m = map(int, input().split())
times = [list(map(int, input().split())) for _ in range(m)]
src, dist = map(int, input().split())
 
print(times)
# 算法入口
def solve(n, times, src, tar):
    # 构建图
    graph = {}
    for u, v, w in times:
        if graph.get(u) is None:
            graph[u] = []
        graph[u].append([v, w])
    print(graph)

    # 初始化源点到每个节点的最短路径
    dist = [sys.maxsize for _ in range(n + 1)]
    dist[src] = 0

    q = [src]
    # used = [False] * (n + 1) # 标记节点是否已确定源点到该节点的最短路径
    while q:
        node = q.pop() # 取出 待确认的节点 中 由源点到待确认的节点的路径最短 的节点

        # if used[node]: # 移到加入q时更高效
        #     continue

        # node是待确认节点中拥有最短路径的节点，因而不存在经过其他待确认节点到达x的路径小于dist[node]
        # 故可以确认由源节点到x节点的最短路径就是dist[node]
        # 如第一轮1->2 = 1, 1->3 = 3, dist[2] = 1, dist[3] = 3,
        # 第二轮从2开始， 有2->4 = 4, 2->5 = 5, 有dist[4] = 5, dist[5] = 6
        # 第三轮的节点将从3，4，5中选择，由于dist[3]最小，第三轮将从3节点开始
        # 若图中存在 4->3 = 1,当遍历4时，经由4到达3的路径为1+2+4+1=8，小于dist[3],不会更新

        # used[node] = True

        # 遍历当前选择的节点中可达的节点，并更新这些节点的最短路径（如果需要更新话），
        # 这些节点如果被更新的话说明还未找到最短路径，需要加入候补队列同时
        if graph.get(node) is not None:
            for v, w in graph[node]:
                # 从源点经最短路到达当前节点后，再到当前连接的其他节点路径
                v_newDist = dist[node] + w 

								# 当前连接的其他节点路径原本的到达方案距离更长则更新并加入候选未确定最短路的节点
                if v_newDist < dist[v]:
                    dist[v] = v_newDist 
                    # if v not in q and not used[node]:
					# not used不需要判断，已被确定的节点不会v_newDist不会小于dist[v]， 由此used可以不需要
                    if v not in q:
                        q.append(v)

        q.sort(key=lambda x : dist[x],  reverse=True)

    return -1 if dist[tar] == sys.maxsize else dist[tar]
 
    
 
 
# 算法调用
print(solve(n, times, src, dist))

'''
3 3
1 2 11
2 3 13
1 3 50
1 3

=24

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
=6

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
=-1
'''