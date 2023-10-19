# 输入获取
m, n, i, j, k, l = map(int, input().split(","))
 
 
# 算法入口
def getResult(m, n, i, j, k, l):
    """
    :param m: 矩阵行数
    :param n: 矩阵列数
    :param i: 扩散点1行号
    :param j: 扩散点1列好
    :param k: 扩散点2行号
    :param l: 扩散点2列号
    :return: 矩阵的所有元素变为1所需要秒数
    """
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    matrix[i][j] = 1
    matrix[k][l] = 1
 
    # count记录未被扩散的点的数量
    count = m * n - 2
 
    # 多源BFS实现队列
    queue = [[i, j], [k, l]]
 
    # 上下左右偏移量
    offsets = ((1, 0), (-1, 0), (0, 1), (0, -1))
 
    day = 1
    # 如果扩散点没有了，或者所有点已被扩散，则停止循环
    while len(queue) > 0 and count > 0:
        newQueue = []
 
        for x, y in queue:
            # 我们假设初始扩散点的1代表第1秒被扩散到的，则下一波被扩散点的值就是1+1，即第2秒被扩散到的
            day = matrix[x][y] + 1
 
            for offsetX, offsetY in offsets:
                newX = x + offsetX
                newY = y + offsetY
 
                if 0 <= newX < m and 0 <= newY < n and matrix[newX][newY] == 0:
                    # 将点被扩散的时间记录为该点的值
                    matrix[newX][newY] = day
                    # 被扩散到的点将变为新的扩散源
                    newQueue.append([newX, newY])
                    # 未被扩散点的数量--
                    count -= 1
 
        queue = newQueue
 
    return day - 1
 
 
# 算法调用
print(getResult(m, n, i, j, k, l))