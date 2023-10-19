# 深度优先搜索

mnk = [int(x) for x in input().split()]
m = mnk[0]
n = mnk[1]
k = mnk[2]
mat = []
for i in range(m):
    mat.append([int(x) for x in input().split()])

class Solution:
    def __init__(self, m, n, k, mat) -> None:
        self.m = m
        self.n = n
        self.k = k
        self.mat = mat

        self.has_search = [[False]*n for i in range(m)]
        self.has_search[0][0] = True
        self.max_height = 0
        self.min_step = m * n
        self.offset = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # 检查是否需要更新结果
    def check(self, i, j, steps):
        if self.max_height == self.mat[i][j]:
            self.max_height = self.mat[i][j]
            self.min_step = min(self.min_step, steps)
        elif self.max_height < self.mat[i][j]:
            self.max_height = self.mat[i][j]
            self.min_step = steps

    def dfs(self, i, j, steps):
        
        # 判断是否越界 以及是否已遍历
        for x, y in self.offset:
            new_i = i + x
            new_j = j + y
            if 0 <= new_i and new_i < self.m and 0 <= new_j and new_j < self.n and self.has_search[new_i][new_j] == False:
                if abs(mat[i][j] - mat[new_i][new_j]) <= self.k: 
                    self.has_search[new_i][new_j] = True
                    self.check(new_i, new_j, steps)
                    self.dfs(new_i, new_j, steps + 1)
                    self.has_search[new_i][new_j] = False

   
s = Solution(m, n, k, mat)
s.dfs(0, 0, 1)

print(s.max_height, s.min_step)

'''
5 4 3
0 2 4 0
3 8 3 1
5 6 7 8
2 10 0 10
3 4 5 8


5 4 1
0 1 2 0
1 0 0 0
1 0 1 2
1 3 1 0
0 0 0 9
'''