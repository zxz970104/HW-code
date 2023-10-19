#include <iostream>
#include <vector>
#include <unordered_map>
#include <regex>
#include <deque>

std::vector<int> split(const std::string& str, const std::string& sep) {
    std::vector<int> res;
    std::regex pattern(sep);
    std::sregex_token_iterator iter(str.begin(), str.end(), pattern, -1);
    std::sregex_token_iterator end;
    while (iter != end) {
        res.push_back(std::stoi(*iter));
        ++iter;
    }
    return res;
}

// 深度优先搜索
void dfs(int id, int& res, std::unordered_map<int, std::pair<int, std::vector<int>>>& map) {
    res += map[id].first;
    if (map[id].second.empty()) {
        return;
    }

    for (auto& item : map[id].second) {
        dfs(item, res, map);
    }
}

int main() {
    int n, target;
    std::cin >> n >> target;
    std::cin.get();
    std::unordered_map<int, std::pair<int, std::vector<int>>> map;
    std::string str;
    for (int i = 0; i < n; i++) {
        getline(std::cin, str);
        std::vector<int> nums = split(str, "[ ,()]+");
        map[nums[0]] = std::make_pair(nums[1], std::vector<int>(nums.begin() + 2, nums.end()));
    }

    // 打印map
    std::cout << "=====================" << std::endl;
    for (auto& it : map) {
        std::cout << it.first << " : " << it.second.first << " ( ";
        for (auto& num : it.second.second) {
            std::cout << num << " ";
        }
        std::cout << ")" << std::endl;
    }
    std::cout << "=====================" << std::endl;

    // 广度优先搜索
    std::deque<int> targets = {target};
    int res1 = 0;
    while (!targets.empty()) {
        int n = targets.size();
        for (int i = 0; i < n; i++) {
            int id = targets[0];
            targets.pop_front();
            res1 += map[id].first;
            for (auto& item : map[id].second) {
                targets.push_back(item);
            }
        }
    }
    std::cout << res1 << std::endl;

    int res2 = 0;
    dfs(target, res2, map);
    std::cout << res2 << std::endl;
}

/*
3 1
3 15 ()
1 20 (2)
2 10 (3)

4 2
4 20 ()
5 30 ()
2 10 (4,5)
1 40 ()
*/