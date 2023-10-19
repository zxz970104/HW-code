N, M, K = [int(x) for x in input().split()]

mat = []
for i in range(N):
    mat.append(input())

diffusion = ((-1, 0), (1, 0), (0, -1), (0, 1))






def bfs(enemy, has_search, res):
    q = [enemy]
    count_enemy = 1
    while q:
        n = len(q)
        for _ in range(n):
            node = q.pop(0)
            for item in diffusion:
                new_row = node[0]+item[0]
                new_col = node[1]+item[1]
                if 0 <= new_row < N and 0 <= new_col < M \
                    and mat[new_row][new_col] != '#' \
                    and has_search[new_row][new_col] == 0:
                    q.append([new_row, new_col])
                    # 1的标志在于避免重复搜索，若本轮搜索中有两个节点（1,1），（2,2），则（1,2）与（2,1）将会被重复加入下一层搜索表
                    has_search[new_row][new_col] = 1 
                    if mat[new_row][new_col] == 'E':
                        count_enemy += 1
            has_search[node[0]][node[1]] = 2
    return count_enemy

def solve(mat):
    
    has_search = [[0]*M for _ in range(N)]
    enemies = []
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 'E':
                enemies.append([i, j])
    res = 0
    for enemy in enemies:
        if has_search[enemy[0]][enemy[1]] == 2:
            continue
        count_enemy = bfs(enemy, has_search, res)
        if count_enemy < K:
            res += 1
    return res

print(solve(mat))     

'''
3 5 2
..#EE
E.#E.
###..
'''
