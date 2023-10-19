import copy

s = input()
s_list = [x for x in s]
n = len(s_list) - int(input())

res = s_list

def dfs(s_list, start, num, path):
    global res
    if num == n:
        if path < res:
            res = copy.deepcopy(path)
        return
    
    for i in range(start, len(s_list)):
        
        
        if path > res: # print(['5', '8'] > ['5', '0', '9']) # True
            continue

        if len(s_list) - i < n - num:
            break

        path.append(s_list[i])
        dfs(s_list, i + 1, num + 1, path)
        path.pop()

dfs(s_list, 0, 0, [])

print(''.join(res))


