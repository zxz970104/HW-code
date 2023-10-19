#include <iostream>
#include <set>
#include <deque>
#include <vector>

// 传输方向
int offset[8][2] = {
    {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}
};


int spfa(std::vector<std::vector<int>> mat, int M, int N) {
    // 标记源点到各个点的最短距离
    int dist[M][N];
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            dist[i][j] = INT_MAX; 
        }
    }
    // set与deque配合用于记录遍历到的点
    std::set<std::pair<int, int>> set_dist;
    std::deque<std::pair<int, int>> queue;
    queue.push_back({0, 0});
    set_dist.insert({0, 0});

    dist[0][0] = mat[0][0]; // 源点到自己的距离为自身
    
    while (!queue.empty()) {
        // 取出本轮要遍历的点
        std::pair<int, int> cur = queue.front();
        int i = cur.first;
        int j = cur.second;

        queue.pop_front();
        set_dist.erase(cur);
        // 遍历8个可传输的方向
        for (int k = 0; k < 8; k++) {
            // 新节点索引
            int new_i = i + offset[k][0];
            int new_j = j + offset[k][1];

            if (new_i >= 0 && new_i < M && new_j >= 0 && new_j < N) { // 索引合法
                int new_dist = dist[i][j] + mat[new_i][new_j]; // 源点传输到当前节点的距离

                // 连续相等的传输时延减1
                if (mat[new_i][new_j] == mat[i][j] && mat[i][j] > 0) { 
                    new_dist--;
                }

                if (new_dist < dist[new_i][new_j]) { // 本次循环中 源点传输到当前节点的距离 比之前短
                    dist[new_i][new_j] = new_dist; // 更新
                    
                    if (set_dist.find(cur) == set_dist.end()) {
                        std::cout << "new: " << new_i << " " << new_j << " " << new_dist << std::endl;
                        queue.push_back({new_i, new_j}); // 加入遍历队列
                    }
                }
            }
        }
    }

    return dist[M-1][N-1];
}

int main() {
    int M, N;
    scanf("%d %d\n", &M, &N);
    std::vector<std::vector<int>> mat(M, std::vector<int>(N, 0));
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &mat[i][j]);
        }
    }

    std::cout << spfa(mat, M, N) << std::endl;
}

/*
3 3
0 2 2
1 2 1
2 2 1

4 5
0 2 3 6 9
4 3 4 3 8
1 2 3 1 7
5 8 6 3 3
*/