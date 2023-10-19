from typing import *
'''
有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，
其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x - 1][y - 1] = time

        dist = [float('inf')] * n
        dist[k - 1] = 0
        used = [False] * n
        for _ in range(n):
            x = -1
            # 找到待确认节点中拥有最短路径的节点
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            # x是待确认节点中拥有最短路径的节点，因而不存在经过其他待确认节点到达x的路径小于dist[x]
            # 故可以确认由源节点到x节点的最短路径就是dist[x]
            used[x] = True 
            # 更新该节点所连接的节点的最短路径
            for y, time in enumerate(g[x]):
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1

# 输入获取
import sys
 
n, m = map(int, input().split())
times = [list(map(int, input().split())) for _ in range(m)]
src, dist = map(int, input().split())

print(Solution().networkDelayTime(times, n, m))