# 输入获取
nums = list(map(int, input().split(",")))
bag = int(input())
 
 
# 算法入口
def getResult():
    n = len(nums)
 
    dp = [0] * (bag + 1)
    dp[0] = 1
 
    for i in range(1, n + 1):
        num = nums[i - 1]
        print(dp)
        for j in range(bag, num-1, -1):
            dp[j] = dp[j] + dp[j - num]
    print(dp)
    return dp[bag]
 
 
# 算法调用
print(getResult())