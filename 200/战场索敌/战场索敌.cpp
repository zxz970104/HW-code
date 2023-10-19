#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <set>

int main() {
    int N, M, K;
    scanf("%d %d %d\n", &N, &M, &K);
    std::vector<std::vector<char>> mat(N, std::vector<char>(M));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%c", &mat[i][j]);    
        }
        scanf("\n");
    }

    std::set<std::pair<int, int>> dir = {{0,-1}, {0, 1}, {-1, 0}, {1, 0}}; // 上下左右
    std::deque<std::pair<int, int>> q; // 存储待搜索的点
    int res = 0;

    std::vector<std::vector<int>> searched(N, std::vector<int>(M, 0)); // 0表示未被搜索， 1表示已加入待搜索队列，2表示完成搜索
    // 从每个点开始搜索
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            // 剪枝，墙不搜索，已被搜索过的不再搜索
            if (mat[i][j] == '#' || searched[i][j] == 2) { 
                continue;
            }
            int enemy_num = 0; // 敌人数量
            q.push_back({i, j}); // 将当前点加入队列
            while (q.empty() == false) {
                std::pair<int, int> cur = q.front(); // 获取被搜索的点
                if (mat[cur.first][cur.second] == 'E') { // 待搜索点为敌人则敌人数量+1
                    enemy_num++;
                }
                // 向四个方向扩散
                for (auto& d : dir) {
                    int new_x = cur.first + d.first;
                    int new_y = cur.second + d.second;
                    // 检查新点是否合法且需要被搜索
                    if (new_x >= 0 && new_x < N && new_y >= 0 && new_y < M 
                        && mat[new_x][new_y] != '#'
                        && searched[new_x][new_y] == 0) { 
                        q.push_back({new_x, new_y});
                        searched[new_x][new_y] = 1; // 标记为已加入待搜索队列,避免重复加入
                    }
                }
                q.pop_front(); // 弹出已被搜索的点
                searched[cur.first][cur.second] = 2; // 标记为已搜索
            }

            if (enemy_num < K) {
                res++;
            }
        }
    }
    
    std::cout << res << std::endl;

    
    
}