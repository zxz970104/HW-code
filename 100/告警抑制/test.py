# https://fcqian.blog.csdn.net/article/details/130768150
import collections

N = int(input())
supress = []
for i in range(N):
    supress.append([x for x in input().split()])

warn = [x for x in input().split()]

# 构建镇压关系图
dict = {}
for item in supress:
    if item[0] in dict:
        dict[item[0]].append(item[1])
    else:
        dict[item[0]] = [item[1]]
print(dict)

# 构建需要被镇压的列表
need_suppressed = []
for it in warn:
    if it in need_suppressed:
        continue
    q = collections.deque()
    q.append(it)
    while q:
        cur = q.popleft()
        if cur in dict:
            need_suppressed.extend(dict[cur])
            q.extend(dict[cur])

print(need_suppressed)

res = []
for it in warn:
    if it not in need_suppressed:
        res.append(it)

print(res)




