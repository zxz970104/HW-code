#include <iostream>
#include <vector>

std::vector<int> split(const std::string& str, char delimiter) {
    std::vector<int> tokens;
    size_t pos = 0;
    size_t found = 0;
    while ((found = str.find(delimiter, pos)) != std::string::npos) {
        tokens.push_back(std::stoi(str.substr(pos,found - pos)));
        pos = found + 1;
    }
    tokens.push_back(std::stoi(str.substr(pos)));
    return tokens;
}

bool isPreOrder(std::vector<int> preorder, int start, int end) {
    if (start >= end) {
        return true
    }
    int rootVal = preorder[start];
    int rightChildInx = start + 1;
    while (preorder[rightChildInx] < rootVal) {
        rightChildInx++;
    }

    for (int i = rightChildInx; i <= end; i++) {
        if (preorder[i] <= rootVal) {
            return false;
        }
    }

    return isPreOrder(preorder, start+1, rightChildInx-1) && isPreOrder(preorder, rightChildInx, end);

}

int main() {
    std::string str;
    getline(std::cin, str);
    std::vector<int> preorder = split(str, ' ');
    bool is_preorder = isPreOrder(preorder, 0, preorder.size()-1);
    std::cout << is_preorder << std::endl;
}