#include <iostream>
#include <vector>

bool isValid(int x, int y) {
    if (y <= 0 || y < x || y - x >= 10) {
        return false;
    } else {
        return true;
    }
}



int get_result(std::vector<int>& vec, int M, int T, int P) {
    int res = 0;
    int left = 0;
    while (left < vec.size() && vec[left] < 0) {
        left++;
    }
    if (left >= vec.size()) {
        return 0;
    } else {
        res++;
    }
    int right = left + 1;
    int err_num = 0;
    while (right < vec.size()) {
        if (isValid(vec[right-1], vec[right])) {
            right++;
        } else {
            err_num++;
            vec[right] = vec[right-1];
            right++;
        }
    }


}


int main() {
    int M, T, P;
    std::cin >> M >> T >> P;
    std::vector<int> vec;
    int sample;
    while (std::cin >> sample) {
        vec.push_back(sample);
    }
    std::cout << get_result(vec, M, T, P) << std::endl;
}

/*


*/