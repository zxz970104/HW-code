#include <iostream>
#include <vector>


bool isMidOrder(const std::vector<int> &midorder) {
    for (int i = 0; i < midorder.size(); i++) {
        if (i > 0 && midorder[i] < midorder[i - 1]) {
            return false;
        }
    }
}

int main() {
    std::vector<int> midorder = {8, 3, 1, 6, 4, 7, 10, 14, 13};

}