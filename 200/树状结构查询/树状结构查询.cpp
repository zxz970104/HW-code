#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <deque>
#include <queue>

using namespace std;

class Node {
    public:
        string name;
        vector<Node*> child;
        Node(string str) {
            this->name = str;
        }
        ~Node() {
            for (size_t i = 0; i < child.size(); i++) {
                if (child[i] != nullptr) {
                    delete child[i];
                    child[i] = nullptr;
                }
            }
        }
};

int main() {
    int n;
    cin >> n;
    // cout << n << endl;
    unordered_map<string, Node*> dict;
    for (int i = 0; i < n; i++) {
        string child_str;
        cin >> child_str;
        string father_str;
        cin >> father_str;
        
        // cout << child_str << " " << father_str << endl;
        
        Node* child_node = nullptr;
        if (dict.find(child_str) == dict.end()) {
            child_node = new Node(child_str);
            dict[child_str] = child_node;
        } else {
            child_node = dict[child_str];
        }

        Node* father_node = nullptr;
        if (dict.find(father_str) == dict.end()) {
            father_node = new Node(father_str);
            dict[father_str] = father_node;
        } else {
            father_node = dict[father_str];
        }
        father_node->child.push_back(child_node);

    }

    string target_str;
    cin >> target_str;
    cout << "------------------------" << endl;

    Node* target_node = dict[target_str];

    deque<Node*> q;
    q.push_back(target_node);
    priority_queue<string, vector<std::string>, greater<std::string>> minHeap;
    while (!q.empty()) {
        size_t n = q.size();
        for (int i = 0; i < n; i++) {
            Node* tmp = q[0];
            q.pop_front();
            minHeap.push(tmp->name);
            for (auto item : tmp->child) {
                q.push_back(item);
            }
        }
    }

    minHeap.pop();
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