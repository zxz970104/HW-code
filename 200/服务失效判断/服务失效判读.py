from collections import deque

inp = input().split(",")

fail = deque(input().split(","))
first = {} # 键为服务，值为第一次出现的位置
graph = {}
for i in range(len(inp)):
    end, start = inp[i].split("-")
    first[start] = first.get(start, i)
    first[end] = first.get(end, i+1)
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]

print(graph)
print(first)
print(fail)

while fail:
    n = len(fail)
    for i in range(n):
        item = fail.popleft()
        first.pop(item)
        if item in graph:
            fail.extend(graph[item])
            graph.pop(item, None) # 避免 a->b, c->b, b->d时b被重复计算

ans = list(first.keys())
ans.sort(key = lambda x : first[x])
print(ans)
