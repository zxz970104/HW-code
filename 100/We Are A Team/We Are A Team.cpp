#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

// 字符串分隔
vector<int> split_int(const string& str, const char ch) {
    vector<int> ret;
    size_t start = 0;
    for (size_t i = 0; i < str.size(); i++) {
        if (str[i] == ch) {
            ret.push_back(stoi(str.substr(start, i - start)));
            start = i + 1;
        }

        if (i == str.size() - 1) {
            ret.push_back(stoi(str.substr(start, i - start + 1)));
        }
    }
    return ret;
}

vector<int> split_int_2(const string& str, const char ch = ' ') {
    istringstream iss(str);
    string token;
    vector<int> ret;
    while(getline(iss, token, ch)) {
        ret.push_back(stoi(token));
    }
    return ret;
}


// 从控制台读取一行并转化为整数列表
vector<int> readline_vec_int(char ch = ' ') {
    string str = "";
    getline(cin, str);
    return split_int_2(str, ch);
}

// 打印vector
template<typename T>
void print_vector(vector<T> &vec) {
    for (auto& v : vec) {
        cout << v << " ";
    }
    cout << endl;
}

// 并查集
class UF {
    public:
        vector<int> father;
        vector<int> rank;
    
    public:
        UF(const int n) {
            this->father.resize(n+1);
            for (int i = 0; i < n+1; i++) {
                father[i] = i;
            }
            this->rank.resize(n+1, 1);
        }

        int find(int i) {
            if (father[i] == i) {
                return i;
            }

            return find(father[i]);
        }

        void merge(int i, int j) {
            int x = find(i);
            int y = find(j);
            if (x == y) {
                return;
            }
            if (rank[x] <= rank[y]) {
                father[x] = y;
            } else {
                father[y] = x;
            }

            if (rank[x] == rank[y] && x != y) {
                rank[y]++;
            }
        }
};


void solve(UF &uf, const int n) {
    vector<int> msg = readline_vec_int();

    if (msg[0] < 1 || msg[0] > n || msg[1] < 1 || msg[1] > n) {
        cout << "da pian zi" << endl;
    }
    if (msg[2] == 0) {
        uf.merge(msg[0], msg[1]);
    } else if (msg[2] == 1) {
        if (uf.find(msg[0]) == uf.find(msg[1])) {
            cout << "we are a team" << endl;
        } else {
            cout << "we are not a team" << endl;
        }
    } else {
        cout << "da pian zi" << endl;
    }
}

int main() {
    vector<int> nm = readline_vec_int();
    int n = nm[0];
    int m = nm[1];
    UF uf = UF(n);

    for (int i = 0; i < m; i++) {
        solve(uf, n);
    }
    return 0;

}

/*
5 7
1 2 0
4 5 0
2 3 0
1 2 1
2 3 1
4 5 1
1 5 1
*/

/*
5 6
1 2 0
1 2 1
1 5 0
2 3 1
2 5 1
1 3 2
*/