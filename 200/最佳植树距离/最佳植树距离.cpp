#include <iostream>
#include <string>
#include <vector>

std::vector<int> split(const std::string& str, char delimiter) {
    std::vector<int> result;
    size_t pos = 0;
    size_t found = 0;
    while ((found = str.find(delimiter, pos)) != std::string::npos) {
        result.push_back(std::stoi(str.substr(pos, found - pos)));
        pos = found + 1;
    }
    result.push_back(std::stoi(str.substr(pos)));
    return result;
}

bool check(int dis, const std::vector<int>& pos, int trees) {
    if (pos.empty()) {
        return false;
    }
    int count = 0;
    int pre = pos[0];
    for (int i = 1; i < pos.size(); i++) {
        if (pos[i] - pre >= dis) {
            count++;
            pre = pos[i];
        }
    }

    return count >= trees;
}

int get_res(const std::vector<int>& pos, int trees) {
    if (pos.size() < 2) {
        return 0;
    }
    int min_dis = 1;
    int max_dis = pos[pos.size()  - 1] - pos[0];
    int res = 0;
    while (min_dis <= max_dis) {
        int mid = ((max_dis - min_dis) >> 1) + min_dis;
        if (check(mid, pos, trees)) {
            res = mid;
            min_dis = mid + 1;
        } else {
            max_dis = mid - 1;
        }
    }
    return res;
}

int main() {
    int n;
    scanf("%d\n", &n);
    std::string line;
    getline(std::cin, line);
    std::vector<int> pos = split(line, ' ');
    int trees;
    std::cin >> trees;
    std::cout << get_res(pos, trees) << std::endl;
}

/*
7
1 5 3 6 10 7 13
3
*/