#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::string str;
    std::getline(std::cin, str);
    int num = atoi(str.c_str());
    int left = 1;
    int right = 1;
    std::vector<std::vector<int>> res;
    while (right < num) {
        int sum = ((right - left + 1) * (left + right)) >> 1;
        if (sum < num) {
            right++;
        } else if (sum > num) {
            left++;
        } else {
            std::vector<int> item;
            for (int i = left; i <= right; i++) {
                item.push_back(i);
            }
            res.push_back(item);
            right++;
        }
    }
    res.push_back(std::vector<int>(1,num));

    for (int i = res.size() - 1; i >= 0; i--) {
        std::cout << num << "=";
        for (int j = 0; j < res[i].size(); j++) {
            if (j == res[i].size() - 1) {
                std::cout << res[i][j] << std::endl;
            } else {
                std::cout << res[i][j] << "+";
            }
        }
    } 
    std::cout << "Result:" << res.size() << std::endl;
    
}