'''
一个背包,往里装东西,重量w(weight)分别为为[2,3,4,5] 价值v(value)对应为[3,4,5,6] 
如果你的容量为8,每个物品有[1,2,3,4]个,求你能装入背包的最大价值。
'''

'''
dp[i][j]表示从前i件物品中选出若干件物品放在容量为j的背包

0-1背包问题中,若取了1件第i个物品,则总容量变为j-W[i],剩下的只能在前i-1件物品中去取了,其最大总价值为dp[i-1][j-W[i]] + v[i]
完全背包问题中,若取了1件第i个物品,则总容量变为j-W[i],剩下的仍可以在前i件物品中去取,其最大总价值为dp[i][j-W[i]] + v[i]

'''

w = [2,3,4,5]
v = [3,4,5,6]
s = [1,2,3,4]
c = 8

'''
比如第i件物品有s个,我可以把相同种类的物品的进行合并,
比如我拿出两件合并出一个新的物品,我拿出三件合并出一个新的物品,以此类推,我拿出s个合并出一个新的物品。
基于这种思想,我们把第i件的s个物品转换为s种体积各不相同的物品,然后在用01背包的思想,求出最优解!
'''

# 直接扩增原有列表，最简便
def solve1():
    new_w = []
    new_v = []
    for i in range(len(s)):
        for j in range(s[i]):
            new_w.append(w[i])
            new_v.append(v[i])

    dp = [0 for _ in range(c+1)]
    # 循环次数 sum(s) * c
    for i in range(1, len(new_w) + 1):
        for j in reversed(range(1, c + 1)):
            if j >= new_w[i-1]:
                dp[j] = max(dp[j], dp[j-new_w[i-1]] + new_v[i-1])
    
    return dp[c]

# 优化一 ：省空间
def solve2():
    dp = [0 for _ in range(c+1)]
    # 循环次数 c * len(w) * [ for x in s[i] ] = c * sum(s)
    for i in range(1, len(w)+1):
        for j in reversed(range(1, c+1)):

            # 多嵌套一次循环，判断第i件物品从拿1件到拿k件的结果
            for k in range(1, s[i-1] + 1):
                if k*w[i-1] <= j:
                    dp[j] = max(dp[j], dp[j-k*w[i-1]]+k*v[i-1])
    return dp[c]


# 优化二： 二进制优化

'''
如某件商品有10件，按第一种需要扩增10个一样的商品用于遍历，按第二种方法需要多循环 10*c 次
10件无非是拿1,2,3,4,5...,10
这里我们之间是直接表示，现在3可以用1+2表示，7可以用1+2+4表示，省去一部分遍历
10表示为：1 2 4 3  3为二进制余下的
'''

def solve3():
    new_w = []
    new_v = []
    # 以二进制方式构建新的物品重量与价值列表
    for i in range(len(s)):
        s_value = s[i]
        k = 1
        while k <= s_value:
            new_w.append(k * w[i])
            new_v.append(k * v[i])
            s_value -= k
            k *= 2

        if s_value > 0:
            new_w.append(s_value * w[i])
            new_v.append(s_value * v[i])

    print(new_w, new_v)

    # 用01背包解决
    dp = [0 for i in range(c+1)]
    for i in range(1, len(new_w) + 1):
        for j in reversed(range(1, c+1)):
            if j >= new_w[i-1]:
                dp[j] = max(dp[j], dp[j-new_w[i-1]] + new_v[i-1])

    return dp[c]

print(solve1())
print(solve2())
print(solve3())

