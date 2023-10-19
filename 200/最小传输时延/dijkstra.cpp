#include <iostream>
#include <vector>
#include <queue>
#include <limits>

class Solution {
public:
    int networkDelayTime(std::vector<std::vector<int>>& times, int N, int K) {
        // 构建图的邻接表表示
        std::vector<std::vector<std::pair<int, int>> > graph(N + 1);
        for (const auto& edge : times) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            graph[u].push_back(std::make_pair(v, w));
        }

        // 初始化距离数组，用于存储从源节点 K 到每个节点的最短时延
        std::vector<int> dist(N + 1, std::numeric_limits<int>::max());
        dist[K] = 0;

        // 使用最小堆（优先队列）来实现 Dijkstra 算法
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
        pq.push(std::make_pair(0, K));

        while (!pq.empty()) {
            int d = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            // 如果当前节点已经访问过，跳过
            if (d > dist[u]) {
                continue;
            }

            // 更新从源节点 K 到邻居节点的最小时延
            for (const auto& neighbor : graph[u]) {
                int v = neighbor.first;
                int w = neighbor.second;
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push(std::make_pair(dist[v], v));
                }
            }
        }

        // 找到最大的最小时延，即最后一个节点收到信号的时延
        int max_delay = 0;
        for (int i = 1; i <= N; i++) {
            if (dist[i] == std::numeric_limits<int>::max()) {
                return -1; // 有不可达的节点
            }
            max_delay = std::max(max_delay, dist[i]);
        }

        return max_delay;
    }
};

int main() {
    int N = 10;
    int K = 1;
    std::vector<std::vector<int>> times = {{1, 2, 5}, {2, 3, 7}, {3, 4, 4}, {4, 5, 6}, {5, 6, 8}, {6, 7, 9}, {7, 8, 10}, {8, 9, 11}, {9, 10, 12}, {10, 1, 13}};

    Solution solution;
    int result = solution.networkDelayTime(times, N, K);
    std::cout << "res: " << result << std::endl; // 104

    return 0;
}
