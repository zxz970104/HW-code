#include <iostream>
#include <vector>
#include <algorithm>

void quick_sort(std::vector<std::pair<int, int>> &vec, int start, int end) {
    if (start >= end) {
        return;
    }
    int i = start;
    int j = end;
    std::pair<int, int> pivot = vec[i];

    while (i < j) {
        // vec[j].second >= pivot.second z这里的=号不能少
        while (i <= j && (vec[i].first > pivot.first || (vec[i].first == pivot.first && vec[i].second >= pivot.second))) {
            i++;
        }
        while (i <= j && (vec[j].first < pivot.first || (vec[j].first == pivot.first && vec[j].second <= pivot.second))) {
            j--;
        }
        if (i < j) {
            std::pair<int, int> temp = vec[i];
            vec[i] = vec[j];
            vec[j] = temp;
        }
    }
    std::pair<int, int> temp = vec[j];
    vec[j] = vec[start];
    vec[start] = temp;
    quick_sort(vec, start, j-1);
    quick_sort(vec, j+1, end);
}

int main() {
    std::vector<std::pair<int, int>> vec;
    std::pair<int, int> p;
    while (std::cin >> p.first >> p.second) {
        vec.push_back(p);
    }
    // 打印vec
    for (auto &p : vec) {
        std::cout << p.first << " " << p.second << std::endl;
    }

    // std::sort(vec.begin(), vec.end(), 
    // [](std::pair<int, int> p1, std::pair<int, int> p2) {
    //     if (p1.first == p2.first) {
    //         return p1.second > p2.second;
    //     } else {
    //         return p1.first > p2.first ;
    //     }
        
    // });

    quick_sort(vec, 0, vec.size()-1);

    // 打印vec
    std::cout << "-----------------" << std::endl;
    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i].first << " " << vec[i].second << std::endl;
    }

}

/*
15 6
15 7
74 2
58 7
25 7
69 8
69 12
69 88
69 12
74 6
89 6
15 52
*/