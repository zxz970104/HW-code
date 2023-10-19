max_height = 0


def check(i, j, steps):
    print(max_height)
    max_height = 5  # 一旦在内部赋值，max_height转为局部变量


def dfs(i, j, steps):
    print(max_height)
    if 10 > 5:
        check(i, j, steps)
dfs(0, 0, 1)