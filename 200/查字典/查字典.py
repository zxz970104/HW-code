inp = [x for x in input().split()]
target = inp.pop(0)
n = int(inp.pop(0))
m = len(target)
res = []
for i in range(n):
    if len(inp[i]) < m:  # 字典中单词长度小于前缀长度自不用计算
        continue
    flag = True
    # 逐个字符比较前缀与单词
    for j in range(m):
        if target[j] != inp[i][j]:
            flag = False
            break
    if flag:
        res.append(inp[i])

print(res)