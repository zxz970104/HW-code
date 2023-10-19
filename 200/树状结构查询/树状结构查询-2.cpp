#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <deque>
#include <queue>

using namespace std;

int main() {
    int n;
    cin >> n;
    // cout << n << endl;
    unordered_map<string, vector<string>> dict; // 用字典记录树结构
    for (int i = 0; i < n; i++) {
        string child_str;
        cin >> child_str;
        string father_str;
        cin >> father_str;
        // cout << child_str << " " << father_str << endl;
        if (dict.find(child_str) == dict.end()) {
            dict[child_str] = vector<string>();
        }
        if (dict.find(father_str) == dict.end()) {
            dict[father_str] = vector<string>();
        }
        dict[father_str].push_back(child_str);
    }
    string target_str;
    cin >> target_str;
    cout << "------------------------" << endl;

    // 层次遍历树
    deque<string> q;
    q.push_back(target_str);
    priority_queue<string, vector<std::string>, greater<std::string>> minHeap; // 最小堆放置遍历的节点值
    while (!q.empty()) {
        size_t n = q.size();
        for (int i = 0; i < n; i++) {
            string tmp = q[0];
            q.pop_front();
            minHeap.push(tmp);
            for (auto item : dict[tmp]) {
                q.push_back(item);
            }
        }
    }

    
    minHeap.pop(); // 不打印根节点
    // 访问并移除优先队列中的顶部元素
    while (!minHeap.empty()) {
        std::cout << minHeap.top() << endl;
        minHeap.pop();
    }
}

/*
5
b a
c a
d c
e c
f d
c
*/