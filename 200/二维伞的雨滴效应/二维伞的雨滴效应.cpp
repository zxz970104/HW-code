#include <iostream>
#include <vector>
#include <string>

// 节点数据结构
class TreeNode {
    public:
        TreeNode(int _val) : val(_val) {}
        TreeNode *left = nullptr;
        TreeNode *right = nullptr;
        int val = 0;
};


std::vector<int> split(const std::string& str, char delimiter) {
    std::vector<int> tokens;
    size_t pos = 0;
    size_t found = 0;
    while((found = str.find(delimiter, pos)) != std::string::npos) {
        tokens.push_back(std::stoi(str.substr(pos, found - pos)));
        pos = found + 1;
    }

    tokens.push_back(std::stoi(str.substr(pos)));
    return tokens;
}

// 递归判断数组是否为二叉搜索树的前序遍历
bool isPreorderBST(TreeNode* root, const std::vector<int>& preorder, int start, int end) {
    // 空节点或只有一个节点必然是二叉搜索树
    if (start >= end) {
        return true;
    }
    int rootVal = preorder[start]; // 标识根节点的值
    // 找到根节点右子节点所在的位置（在数组中的索引）
    int rightChildPos = start + 1;
    while (preorder[rightChildPos] < rootVal) {
        rightChildPos++;
    }

    // 检验右子树上的节点是否都大于根节点
    for (int i = rightChildPos; i <= end; i++) {
        if (preorder[i] < rootVal) {
            return false;
        }
    }

    // 递归检验左右数组是否是二叉搜索树的前序遍历
    bool leftChildValid = true, rightChildValid = true;
    if (rightChildPos > start + 1) {
        root->left = new TreeNode(preorder[start + 1]);
        leftChildValid = isPreorderBST(root->left, preorder, start + 1, rightChildPos - 1);
    }

    if (rightChildPos <= end) {
        root->right = new TreeNode(preorder[rightChildPos]);
        rightChildValid = isPreorderBST(root->right, preorder, rightChildPos, end);
    }
    return leftChildValid && rightChildValid;
}

// 获取左伞坠信息
int getLeft(TreeNode* root, int level) {
    // 如果当前节点存在左子节点，递归其左子节点
    if (root->left != nullptr) {
        return getLeft(root->left, level + 1);
    }

    if (level == 0) { // 当前节点是根节点且没有左子节点，则必然没有左伞坠
        return 0;
    } else {
        if (root->right != nullptr) { // 当前节点存在右子节点，则递归其右子节点
            return getLeft(root->right, level + 1);
        } else { // 当前节点无子节点，则当前节点的值便是伞坠的值
            return root->val;
        }
    }
}

int getRight(TreeNode* root, int level) {
    if (root->right != nullptr) {
        return getRight(root->right, level + 1);
    }

    if (level == 0) {
        return 0;
    } else {
        if (root->left != nullptr) {
            return getRight(root->left, level + 1);
        } else {
            return root->val;
        }
    }
}

void printTree(TreeNode* root) {
    // 前序遍历
    if (root == nullptr) {
        return;
    }
    std::cout << root->val << " ";
    printTree(root->left);
    printTree(root->right);
}

int main() {
    std::string str;
    getline(std::cin, str);
    std::vector<int> nums = split(str, ' ');
    TreeNode* root = new TreeNode(nums[0]);
    bool result = isPreorderBST(root, nums, 0, nums.size() - 1);
    if (result) {
        std::cout << result << " " << getLeft(root, 0) << " " << getRight(root, 0) << std::endl;
    } else {
        std::cout << result << " " << 0 << " " << 0 << std::endl;
    }
    printTree(root);

}

/*
8 3 1 6 4 7 10 14 13
*/