#include <iostream>
#include <string>
#include <vector>
#include <sstream>


std::vector<int> split(std::string str, char sep = ' ') {
    std::vector<int> vec;
    size_t pos = 0;
    size_t found;
    while ((found = str.find(sep, pos)) != std::string::npos) {
        vec.push_back(std::stoi(str.substr(pos, found - pos)));
        pos = found + 1;
    }
    vec.push_back(std::stoi(str.substr(pos)));
    return vec;
}

int get_result(const std::vector<int> &vec, const int cap) {
    size_t n = vec.size();
    std::vector<int> dp(cap+1, 0);
    dp[0] = 1;
    for (int i = 1; i < n + 1; i++) { // 遍历物品装还是不装
        for (int j = cap; j >= vec[i - 1]; j--) { // 不同的背包容量下，装满时当前物品不装的方案数与装的方案数之和
            dp[j] = dp[j] + dp[j - vec[i - 1]]; // 装满的方案是当前物品不装的方案数与装的方案数之和
        }
    }
    // for (int i = 0; i < cap + 1; i++) {
    //     std::cout << dp[i] << " ";
    // }
    // std::cout << std::endl;
    return dp[cap];
}

int main() {
    std::string peoples;
    getline(std::cin, peoples);
    std::vector<int> vec = split(peoples, ',');

    int cap;
    std::cin >> cap;

    std::cout << get_result(vec, cap) << std::endl;


}