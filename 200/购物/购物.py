nk = [int(x) for x in input().split()]
n = nk[0]
k = nk[1]

goods_price = [int(price) for price in input().split()]

goods_price.sort()

res = []

def dfs(start, num):
    res.append(num)
    for i in range(start, n):
        num += goods_price[i]
        dfs(i + 1, num)
        num -= goods_price[i]

dfs(0, 0)

res.sort()
print(res)
for i in range(1, k+1):
    print(res[i])