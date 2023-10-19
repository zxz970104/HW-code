arr = [int(x) for x in input().split()]
target = int(input())

def solve():
    dic = {}
    for x in arr:
        if target - x in dic: # x是当前的，target-x是需要的，如果target-x在dic中说明两个数都在arr中
            return target - x, x
        dic[x] = 1 # 等于什么不重要，有就行

def solve2():
    dic = {}
    n = len(arr)
    for i in range(n):
        dic[arr[i]] = dic.get(arr[i], []).append(i) # 该值所处的坐标
    for x in arr:
        # x == target-x需要避免重复使用
        if target - x in dic and (x != target -x or (len(dic[target-x]) > 1 and x == target - x)): 
            return x, target - x

print(solve2())