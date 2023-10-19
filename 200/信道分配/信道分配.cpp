#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;


// int solve(vector<bool> &used, const vector<int> &count, const vector<long> &value, const int D) {
//     bool flag = true;
//     size_t n = count.size();
//     while (flag == true) {
//         for 
//     }


// }

template <typename T>
void print_vector(std::vector<T> &v) {
    for (int i = 0; i < v.size(); i++) {
        std::cout << v[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    // 读取R
    string str = "";
    getline(cin, str);
    stringstream iss_1(str);
    int R = 0;
    iss_1 >> R;

    // 读取每阶信道数
    getline(cin, str);
    stringstream iss_2(str);
    int num = 0;
    vector<int> count;
    while (iss_2 >> num) {
        count.push_back(num);
    }
    // for (int i = 0; i < count.size(); i++) {
    //     cout << count[i] << endl;
    // }

    //读取D
    getline(cin, str);
    stringstream iss_3(str);
    int D = 0;
    iss_3 >> D;

    cout << "D = " << D << endl;

    // 统计单一信道可满足的数量
    int n = 0; // n为需要参与减法的阶数
    int res = 0;
    for (int i = 0; i < R + 1; i++) {
        if ((1 << i) < D) {
            n++;
        } else {
            res += count[i];
        }  
    }
    cout << "res = " << res << endl;

    // 二进制表示D并把每一位逆序放入数组
    int bit[n] = {0};
    for (int i = n - 1; i >= 0; i--) {
        bit[i] = (D >> i) & 1;
        cout << bit[i] << endl;
    }

    while (true) {
        print_vector(count);
        for (int i = n - 1; i > 0; i--) {
            count[i] -= bit[i];
            if (i > 0 && count[i] < 0) { // 不够，需要向左借位
                count[i-1] -= abs(count[i]) << 1;
                count[i] = 0;
            }
        }

        print_vector(count);

        if (count[0] < 0) { // 第一轮减法后，首位为负，进一步检验
            for (int i = 0; i < n-1; i++) {
                if (count[i] < 0) {
                    count[i+1] -= (abs(count[i]) >> 1) + 1;
                    count[i] = 0;
                }
            }
        }
        print_vector(count);

        if (count[n-1] < 0) {
            break;
        }

        res++;
        cout << "==============" << endl;
    }
    
    cout << "res = " << res << endl;
}

/*
5
10 5 0 1 3 2
30

5
10 5 0 1 3 2
47
*/