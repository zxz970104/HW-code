#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_set>

// 例子：0 1 2 3 4  3.5  返回4
int search(const std::vector<int> &pricks, int ability) {
    int left = 0;
    int right = pricks.size() - 1;
    int mid;
    while (left <= right) { // (left + right) >> 1 总是倾向于左侧，而这里希望偏右侧，所以要加=，后面==时也是要+1
        mid = (left + right) >> 1;
        if (pricks[mid] == ability) {
            return mid + 1;
        } else if (pricks[mid] > ability) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

int main() {
    // 读取控制台输入
    int n, m, k;
    scanf("%d %d %d\n", &n, &m, &k);

    std::string ct_str;
    std::getline(std::cin, ct_str);
    std::istringstream iss1(ct_str);
    std::unordered_set<int> ct_set;
    int ct;
    while (iss1 >> ct) {
        ct_set.insert(ct);
    }

    std::string ability_str;
    std::getline(std::cin, ability_str);
    std::istringstream iss2(ability_str);
    std::vector<int> ability_num;
    int ability;
    while (iss2 >> ability) {
        ability_num.push_back(ability);
    }



    std::cout << "n = " << n << std::endl;
    std::cout << "m = " << m << std::endl;
    std::cout << "k = " << k << std::endl;

    std::cout << "ct_set = ";
    for (auto& item : ct_set) {
        std::cout << item << " ";
    }
    std::cout << std::endl;

    std::cout << "ability_num = ";
    for (auto& item : ability_num) {
        std::cout << item << " ";
    }
    std::cout << std::endl;


    std::vector<int> pricks;
    int unhappy = 0;
    for (int i = 0; i < n; i++) {
        std::cout << "pricks = ";
        for (auto& item : pricks) {
            std::cout << item << " ";
        }
        std::cout << std::endl;
        std::cout << "ability_num[i] = " << ability_num[i] << std::endl;


        int rank = search(pricks, ability_num[i]); // 当前学生的能力值在刺头中的排名
        std::cout << "rank = " << rank << std::endl;
        // 不是刺头
        if (ct_set.find(i) == ct_set.end()) {
            unhappy += pricks.size() - rank;
        // 是刺头
        } else {
            pricks.insert(pricks.begin() + rank, ability_num[i]); // 根据能力值排名插入就可以保持有序
        }
    }

    if (unhappy > k) {
        std::cout << 1 << std::endl;
    } else {
        std::cout << 0 << std::endl;
    }

}