# 多源bfs

from collections import deque
m = 5
n = 5
x = [1, 1]
y = [3, 3]
matrix = [[0] * n for _ in range(m)] # 标识节点是否已加入扩散队列
matrix[x[0]][x[1]] = 1
matrix[y[0]][y[1]] = 1
print(matrix)

orientaion = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 扩散规则

count = 2
q = deque()
q.append(x)
q.append(y)
time = 0
#while count < m*n:
while q:
    # 第几轮扩散，即多少秒，
    #注意最后一轮扩散时，队列里的节点已被扩散了（即已被置为1），
    # 次轮不再像队列中加入节点，最终退出循环。但实际这轮+1没有必要，因为此时已经完全扩散了
    time += 1 
    
    len_q = len(q)
    for i in range(len_q):
        node = q.popleft()
        for item in orientaion: # 向上下左右扩散
            new_row = node[0] + item[0]
            new_col = node[1] + item[1]
            if 0 <= new_row < m and 0 <= new_col < n:
                # 未被扩散的节点置为1，加入下一轮扩散节点列表
                if matrix[new_row][new_col] != 1:
                    matrix[new_row][new_col] = 1
                    count += 1
                    q.append([new_row, new_col])
    print(q)

# print(time)
print(time-1)