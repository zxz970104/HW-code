#include <stdio.h>
#include <stdlib.h>

static char tar[10] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
int check(char ch) {
    for (int i = 0; i < 10; i++) {
        if (tar[i] == ch) {
            return 0;
        }
    }
    return -1;
}

int solve(const char str[], const int n) {
    int ret = 0;
    int left = 0;
    int right = 0;

    int flaw_count = 0; // 统计窗口中非元音字母的个数

    /*
    标识当前窗口是否有满足要求的元音字符串，瑕疵数超过目标值时需要考虑
    考虑dfaaacfiiivcuuuuu，瑕疵数目标为2，当right遍历到iii后的v时,窗口中的瑕疵数超过，此时窗口中有满足要求的元音字符串
    考虑sdaaffgsgiu， 瑕疵数目标为2，当right遍历到g时，窗口瑕疵数超过，此时窗口中没有满足要求的元音字符串
    */
    int update = 0;  

    /*
    标识下一次寻找，left指针应指向何处
    考虑dfaaacfiiivcuuuuu, aaacfiii是一个2瑕疵度的元音字符串，
    遍历过程中right指向第三个i，但下一次遍历，left应是从第一个i开始
    */
    int next_left = -1;
    

    while (right != '\0') {

        // 刚开始使left与right共同指向元音字母
        if (right == 0) {
            while (right != '\0') {
                if (check(str[right]) == 0) {
                    left = right;
                } else {
                    right++;
                }
            }
        }

        if (check(str[right]) == 0) {
            if (flaw_count == n) { // 此时窗口包含的是一个满足要求的元音字符串，检验其长度
                if (right - left + 1 > ret) {
                    ret = right - left + 1;
                }
                right++;
                update = 1; // 标识窗口中存在满足要求的元音字符串
            }
        } else {
            flaw_count++; // 瑕疵数增加
            if (flaw_count == n) { 
                right++;
                next_left = right;
            } else if (flaw_count < n) { 
                right++;
            } else if (flaw_count > n) {
                if (update == 0) {
                    while (right != '\0') {
                        if (check(str[right]) == 0) {
                            left = right;
                        } else {
                            right++;
                        }
                    }
                } else {
                    left = next_left;
                    update = 0;
                }
                
            }
              
        }
    }
    return ret;
}

int main() {
    int num;
    scanf("%d", &num);
    fgetc(stdin); // 读出第一行的换行符，否则会影响第二行读取

    char input[65535];
    char* str = fgets(input, sizeof(input), stdin);
    int ret = solve(str, num);
    printf("%d\n", ret);
}