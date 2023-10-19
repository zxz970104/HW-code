'''
一个背包，往里装东西，重量w(weight)分别为为[2,3,4,5] 价值v(value)对应为[3,4,5,6] 
如果你的容量为8,每个物品只有一个，求你能装入背包的最大价值
'''

'''
dp[i][j]表示  只考虑前i个物品, 容量为j时, 背包所能容纳的最大价值
dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1]) if j>= w[i-1] else dp[i-1][j]
'''

w = [2,3,4,5]
v = [3,4,5,6]
c = 8

def solve():
    # 构建dp数组
    dp = [[0] * (c+1) for i in range(len(w)+1)]
    # 外层遍历前i个物品参与拿取
    for i in range(1, len(w)+1):
        # 内层遍历不同背包容量时的可拿物品的最大价值
        for j in range(1, c+1):
            if j >= w[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(w)][c]

def solve2():
    dp = [0 for i in range(c+1)]
    for i in range(1, len(w)+1):
        '''
        逆序原因：
            未一维化时可以看到dp[i][j]需要使用上一层dp[i-1]的结果，若此时仍使用顺序，那么当第一层更新完成遍历第二层时
            dp[j-w[i-1]]将会被先更新，等到更新dp[j]时使用的将是本层的结果而不是上一层的了
            若是逆序则可以保证每次更新本层时用到的都是上一层的信息
        '''
        for j in range(c, 0, -1):
            if j >= w[i-1]:
                dp[j]= max(dp[j], dp[j-w[i-1]] + v[i-1])
    return dp[c]


print(solve())
print(solve2())