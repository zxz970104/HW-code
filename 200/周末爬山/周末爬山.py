import collections

offset = ((-1, 0), (1, 0), (0, -1), (0, 1))

# 广度优先搜索
def bfs(m, n, k, mat):
    step_num = [[0]*n for i in range(m)]
    step_num[0][0] = float("inf")
    q = collections.deque()
    q.append([0,0])

    max_height = 0
    steps = m * n

    count = 0 # 记录当前步数
    while q:
        count += 1
        length = len(q)
        for i in range(length):
            node = q.popleft()

            # 上下左右遍历
            for x, y in offset:
                new_i = node[0] + x
                new_j = node[1] + y
                # 判断是否越界 以及是否已遍历
                if 0 <= new_i and new_i < m and 0 <= new_j and new_j < n and step_num[new_i][new_j] == 0:
                    # 判断是否可达
                    if abs(mat[node[0]][node[1]] - mat[new_i][new_j]) <= k: 
                        step_num[new_i][new_j] = count # 记录到达这个位置的最小步数

                        if max_height < mat[new_i][new_j]:
                            max_height = mat[new_i][new_j]
                            steps = count
                        elif max_height == mat[new_i][new_j]:
                            steps = min(steps, count)

                        q.append([new_i, new_j]) # 加入遍历列表

    print(step_num)

    return max_height, steps


mnk = [int(x) for x in input().split()]
m = mnk[0]
n = mnk[1]
k = mnk[2]
mat = []
for i in range(m):
    mat.append([int(x) for x in input().split()])

# m = 5
# n = 4
# k = 1
# mat = [
#     [0, 1, 2, 0],
#     [1, 0, 0, 0],
#     [1, 0, 1, 2],
#     [1, 3, 1, 0],
#     [0, 0, 0, 9]
# ]

max_height, steps = bfs(m, n, k, mat)
print(max_height, steps)

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

