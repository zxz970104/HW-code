inp = [[int(i) for i in x.strip("[]").split(",")] for x in input().split("],")]

import copy
graph = {} 
res = {} # 记录每位师傅有几个徒弟的名次由于他
for rel in inp:
    if rel[0] in graph:
        graph[rel[0]].append(rel[1])
    else:
        graph[rel[0]] = [rel[1]]
    
    res[rel[0]] = 0
    # 防止有些没徒弟的不被记录
    if res[1] not in res:
        res[rel[1]] = 0
print(graph)
# 从每一个节点开始深度优先搜索
for k,v in graph.items():
    count = 0
    q = copy.deepcopy(v)
    has_search = set() # 考虑环以及重复搜索，如示例1中搜索2时直接搜索4，1。之后4又在搜索1时再次被搜索
    has_search.add(k)
    while q:
        n = len(q)
        for i in range(n):
            x = q.pop(0)
            if x < k:  # 徒弟/徒弟的徒弟/... 名次优于被搜索的师傅
                count += 1
            # elif x == k:  # 注意这中方式不可取，这种只可防A->B, B->C, C->A的环， 无法防范A->B, B->C, C->D, D->B的环
            elif x in has_search:
                continue
            if x in graph:  # 将徒弟加入遍历
                q += graph[x]
            has_search.add(x)
    res[k] = count
print(res)
ans = [v for _, v in sorted(res.items(), key=lambda item : item[0])]
print(ans)




# [[1,4],[1,3],[2,4],[2,1],[3,2]]   0 1 2 0
# [[1,4],[1,3],[2,4],[3,2],[4,5],[5,3]] 0 0 1 2 3