#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::vector<int> split(std::string str, char delimiter) {
    size_t pos = 0;
    size_t found = 0;
    std::vector<int> result;
    std::string s;
    while ((found = str.find(delimiter, pos)) != std::string::npos) {
        result.push_back(std::stoi(str.substr(pos, found - pos)));
        pos = found + 1;
    }
    result.push_back(std::stoi(str.substr(pos)));
    return result;
}

int main() {
    std::string str;
    getline(std::cin, str);
    std::vector<int> nums = split(str, ' ');

    int negative = 0; // 逃脱的负值数量
    std::vector<int> postivite;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > 0) { // 遇到正值直接入栈
            postivite.push_back(nums[i]);
        } else { // 遇到负值
            while (true) {
                // 查看栈是否为空，为空则表明负值逃脱，negative+1，跳出while
                if (postivite.empty()) {
                    negative++;
                    break;
                }
                // 弹出栈顶元素，并计算其和负值的和
                int tmp = postivite.back();
                postivite.pop_back();
                int pk = tmp + nums[i];

                if (pk > 0) { // 消灭了负值，将剩余正值入栈，结束while
                    postivite.push_back(pk);
                    break;
                } else if (pk < 0) { // 被负值消灭，继续派出栈中正值消灭剩余的负值
                    nums[i] = pk;
                } else { // 同归于尽结束while
                    break;
                }

            }
        }
        
    }

    std::cout << postivite.size() + negative << std::endl;

}

/*
5 10 8 -8 5
2 3 4 -10 20 -5 -6 -1 12
-1 -2 -3 10 -5 6 -30 1 2 3
*/