#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;
int main() {
    string src = "";
    getline(cin, src);
    string tar = "";
    getline(cin, tar);

    //找出原字符串中目标字符串的第一个字符所在的位置
    vector<int> src_start;
    size_t tar_i = 0; // 记录目标字符串后续该从哪里开始比较，如b[cd],第一个字符被找出后就需要从[开始匹配
    if (tar[0] == '[') { //出现了[]需要找出所有在[]中的字符
        // 将[]中的字符放入ch_set
        unordered_set<char> ch_set;
        size_t k = 1;
        while (tar[k] != ']') {
            ch_set.insert(tar[k]);
            k++;
        }
        tar_i = k + 1;

        // 找出ch_set中的字符在原字符串中出现的位置
        for (size_t j = 0; j < src.size(); j++) {
            if (ch_set.find(src[j]) != ch_set.end()) {
                src_start.push_back(j);
            }
        }
        
    } else {
        for (size_t i = 0; i < src.size(); i++) {
            if (src[i] == tar[0]) {
                src_start.push_back(i);
            }
        }
        tar_i = 1;
    }

    // 从刚才记录的位置开始逐个字符比较
    for (size_t i = 0; i < src_start.size(); i++) {
        size_t src_idx = src_start[i] + 1;
        size_t tar_idx = tar_i;

        bool has_find = true;
        while (src_idx < src.size() && tar_idx < tar.size()) {
            if (tar[tar_idx] == '[') {
                tar_idx++;
                bool in = false;
                while (tar[tar_idx] != ']') {
                    if (tar[tar_idx] == src[src_idx]) {
                        src_idx++;
                        in = true;
                    }
                    tar_idx++;
                }
                tar_idx++;

                if (!in) {
                    has_find = false;
                    break;
                }
            } else if (tar[tar_idx] != src[src_idx]) { 
                has_find = false;
                break;
            } else if (tar[tar_idx] == src[src_idx]) {
                src_idx++;
                tar_idx++;
            }
        }
        if (has_find) {
            printf("%d\n", src_start[i]);
            exit(0);
        }
    }

    printf("%d\n", -1);
}


// #include <regex>
// int main() {
//     string src = "";
//     getline(cin, src);
//     string tar = "";
//     getline(cin, tar);

//     regex reg(tar);
//     smatch matches;
//     bool has_find = regex_search(src, matches, reg);
//     if (has_find) {
//         printf("%d\n", matches.position());
//     } else {
//         cout << -1 << endl;
//     }

// }