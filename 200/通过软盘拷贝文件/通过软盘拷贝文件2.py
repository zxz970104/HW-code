N = int(input())
files = []

weight = [0]
value = [0]
capcity = 1474560 >> 9 # 2880
# 构建文件实际大小与需要占用的大小
for i in range(N):
    size = int(input())
    if size % 512 == 0: # 可除尽，实际大小与占用大小相同
        true_size = size 
    else:
        k = size >> 9 # 移位操作符效率更高，得到商
    weight.append(k+1)
    value.append(size)

print(weight)
print(value)
print(capcity)

def solve():
    dp = [0] * (capcity + 1)

    for i in range(len(weight)):
        for j in reversed(range(1, capcity+1)):
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j-weight[i]] + value[i]) 
    return dp[capcity]

print(solve())
    



'''
3
737270
737272
737288

6
400000
200000
200000
200000
400000
400000
'''