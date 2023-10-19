#include <stdio.h>
#include <stdlib.h>
#include <string.h>


static char tar[10] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

// 检查字符是否为元音字母
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


    int idx[65535]; // 所有元音字母在字符串中的索引
    memset(idx, -1, sizeof(idx));

    int k = 0;
    for (int i = 0; i < 65535; i++) {
        if (str[i] == '\0') {
            break;
        }

        if (check(str[i]) == 0) {
            idx[k++] = i;
        }
    }

    // int x = 0;
    // printf("idx = ");
    // while (idx[x] != -1)
    // {
    //     printf("%d ", idx[x]);
    //     x++;
    // }
    // printf("\n");


    int l = 0;
    int r = 0;
    int diff = 0; // 瑕疵度
    while (r < k) {

        // 两个元音字母之前有多少个字母 - 两个元音字母之间有多少个元音字母 = 两个元音字母之间有多少个非元音字母
        diff = (idx[r] - idx[l] - 1) - (r - l - 1);

        if (diff > n) {
            l++;
        } else if (diff < n) {
            r++;
        } else {
            int tmp = idx[r] - idx[l] + 1;
            ret = ret < tmp ? tmp : ret;
            r++;
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
    if (strlen(str) == 0) {
        printf("%d\n", 0);
    } else {
        int ret = solve(str, num);
        printf("ret = %d\n", ret);
    }
    return 0;
    
}

// asdbuiodevauufgh