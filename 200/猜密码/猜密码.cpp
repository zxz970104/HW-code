#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>


void dfs(const std::vector<int>& nums, std::vector<std::vector<int>>& res, std::vector<int>& path, int min, int start) {
    if (path.size() >= min) {
        std::vector<int> tmp = path;
        res.push_back(tmp);
    }

    for (int i = start; i < nums.size(); i++) {
        path.push_back(nums[i]);
        dfs(nums, res, path, min, i + 1);
        path.pop_back();
    }
}


int main() {
    std::vector<int> nums;
    char ch;
    while ((ch = getchar()) != '\n') {
        if (ch == ',') {
            continue;
        }
        nums.push_back(ch - '0');
    }
    int min = getchar() - '0';

    std::sort(nums.begin(), nums.end());

    std::vector<std::vector<int>> res;
    std::vector<int> path;
    dfs(nums, res, path, min, 0);
    for (auto& item : res) {
        for (int i = 0; i < item.size(); i++) {
            if (i == item.size() - 1) {
                std::cout << item[i] << std::endl;
            } else {
                std::cout << item[i] << ",";
            }
        }
    }
}