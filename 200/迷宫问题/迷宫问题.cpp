#include <iostream>
#include <vector>
#include <sstream>
#include <deque>


using namespace std;

// 上下左右移动
static vector<pair<int,int>> my_move = {{-1,0}, {1, 0}, {0, -1}, {0, 1}};

// 读取输入的地图
vector<vector<int>> read_matrix(int n, int m) {
    vector<vector<int>> mat;
    string str;
    vector<int> vec;
    for (int i = 0; i < n; i++) {
        getline(cin, str);
        istringstream iss(str);
        int num;
        while (iss >> num) {
            vec.push_back(num);
        }
        mat.push_back(vec);
        vec.clear();
    }
    return mat;
}

// 校验移动到的下一节点是否有效
bool valid(vector<vector<int>>& mat, int row, int col) {
    if (row >= 0 && row < mat.size() && col >= 0 && col < mat[0].size()) {
        if (mat[row][col] == 0) {
            return true;
        }
    }
    return false;
}



vector<vector<pair<int, int>>> solve(vector<vector<int>>& mat) {
    int rows = mat.size();
    int cols = mat[0].size();

    vector<vector<pair<int, int>>> pre(rows, vector(cols, pair(-1, -1))); // 记录节点的前一节点

    deque<pair<int, int>> q; // 广度优先搜索的队列

    q.push_back(pair(rows-1, cols-1)); // 初始将起始节点放入搜索队列，这里倒着搜索是为了更方便顺序打印

    while (!q.empty()) {
        int n = q.size(); 
        for (int i = 0; i < n; i++) {
            pair<int, int> node = q[0];
            q.pop_front();
            
            // 到达目标
            if (node.first == 0 && node.second == 0) {
                return pre;
            }

            //搜索节点，把可达点加入下一轮搜索
            for (auto& item : my_move) {
                int new_row = node.first + item.first;
                int new_col = node.second + item.second;
                if (valid(mat, new_row, new_col)) {
                    q.push_back(pair(new_row, new_col)); // 把可达点加入下一轮搜索
                    
                    pre[new_row][new_col] = node; // 记录下一轮搜索的节点的前一节点，如pre[0][0] = pair(1,0)

                    mat[node.first][node.second] = 2; // 节点即将在下一轮被遍历
                }
            }

            mat[node.first][node.second] = 3; // 节点被遍历完成

        }
    }
    return pre;
}


int main() {
    int n , m;
    string nm;
    getline(cin, nm);
    istringstream iss(nm);
    iss >> n;
    iss >> m;
    vector<vector<int>> mat = read_matrix(n, m);


    vector<vector<pair<int, int>>> ret = solve(mat);

    // 打印结果
    pair<int, int> path = ret[0][0];
    cout << "(0,0)" << endl;
    while (path.first != -1) {
        cout << "(" << path.first << "," << path.second << ")" << endl;
        path = ret[path.first][path.second];
    }

    return 0;
    
}

/*
5 5
0 1 0 0 0
0 1 1 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0

5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 1
0 1 1 1 0
0 0 0 0 0
*/