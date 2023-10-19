'''
一个背包,往里装东西,重量w(weight)分别为为[2,3,4,5] 价值v(value)对应为[3,4,5,6] 
如果你的容量为8,每个物品有无数个,求你能装入背包的最大价值。
'''

'''
dp[i][j]表示从前i件物品中选出若干件物品放在容量为j的背包

区别之处：
0-1背包问题中,若取了1件第i个物品,则总容量变为j-W[i],剩下的只能在前i-1件物品中去取了,其最大总价值为dp[i-1][j-W[i]] + v[i]

完全背包问题中,若取了1件第i个物品,则总容量变为j-W[i],剩下的仍可以在前i件物品中去取,其最大总价值为dp[i][j-W[i]] + v[i]
'''

w = [2,3,4,5]
v = [3,4,5,6]
c = 8

def solve():
    dp = [[0] * (c+1) for i in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for j in range(1, c+1):
            if j >= w[i-1]:
                # 与01背包不同之处dp[i-1][j-w[i-1]] -> dp[i][j-w[i-1]]
                dp[i][j] = max(dp[i-1][j], dp[i][j-w[i-1]] + v[i-1]) 
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(w)][c]

def solve2():
    dp = [0 for i in range(c+1)]
    for i in range(1, len(w)+1):
        for j in range(1, c+1):
            if j >= w[i-1]:
                dp[j]= max(dp[j], dp[j-w[i-1]] + v[i-1])
    return dp[c]

print(solve())
print(solve2())