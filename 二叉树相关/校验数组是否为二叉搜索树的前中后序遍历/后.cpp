#include <iostream>
#include <vector>

bool isPostOrder(const std::vector<int>& postorder, int start, int end) {
    if (start >= end) {
        return true;
    }
    int rootVal = postorder[end]; // 后续遍历的根节点在最后遍历
    // 找到左右子树分界点
    int rightChildInx = 0;
    while (postorder[rightChildInx] < rootVal) {
        rightChildInx++;
    }
    // 查看分界点及后续节点的值是否满足大于根节点
    for (int i = rightChildInx; i < end; i++) {
        if (postorder[i] <= rootVal) {
            return false;
        }
    }
    return isPostOrder(postorder, start, rightChildInx - 1) && isPostOrder(postorder, rightChildInx, end - 1);
}

int main() {
    std::vector<int> postorder = {1,4,7,6,3,13,14,10,8};
    bool result = isPostOrder(postorder, 0, postorder.size() - 1);
    std::cout << result << std::endl;
}