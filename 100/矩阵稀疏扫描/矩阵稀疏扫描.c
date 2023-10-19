#include <stdio.h>

int main() {
    int rows, cols;
    scanf("%d %d", &rows, &cols);
    int mat[rows][cols];

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &mat[i][j]);
        }
    }


    int row_count[100] = {0}; // 数组长度无法再运行时确定
    int col_count[100] = {0}; // 记录第j列中为0元素的个数
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (mat[i][j] == 0) {
                row_count[i]++;
                col_count[j]++;
            }
        }
    }


    int res_row = 0;
    for (int i = 0; i < rows; i++) {
        if ( row_count[i] > (cols >> 1) ) {
            res_row++;
        }
    }
    printf("%d\n", res_row);

    int res_col = 0;
    for (int i = 0; i < cols; i++) {
        if ( col_count[i] > (rows >> 1) ) {
            res_col++;
        }
    }
    printf("%d\n", res_col);
}