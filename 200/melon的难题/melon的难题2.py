n = int(input())
weight = [int(x) for x in input().split()]





def solve():
    weight.sort(reverse=True)
    total = sum(weight)

    if total % 2 != 0:
        return -1
    
    target = total // 2

    dp = [n]* (target + 1)
    dp[0] = 0

    for i in range(1,target+1):
        for j in range(1, len(weight) + 1):
            if i - weight[j-1] >= 0:
                dp[i] = min(dp[i-weight[j-1]]+1,dp[i])

    if dp[target] >= n:
        return -1
    print(dp)
    return dp[target]


def solve2():
    weight.sort(reverse=True)
    total = sum(weight)

    if total % 2 != 0:
        return -1
    
    target = total // 2

    dp = [[n]*(target+1) for i in range(n+1)]
    dp[0][0] = 0

    for i in range(1, len(weight)+1):
        num = weight[i-1]
        for j in range(1, target+1):
            if j < num:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-num] + 1)

    if dp[n][target] == n:
        return -1
    
    return min(n-dp[n][target], dp[n][target])       
        

print(solve2())