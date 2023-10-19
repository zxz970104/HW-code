N = int(input())

inp = []
for i in range(N):
    inp.append([int(x) for x in input().split()])


def getMaxRespTime(time):
    if time < 128:
        return time
    mant = time & 15
    exp = (time & 112) >> 4
    return (0x10 | mant) << (exp+3)


def solve(report):
    res = float("inf")
    for item in report:
        res = min(item[0]+getMaxRespTime(item[1]), res)

    return res

print(solve(inp))

'''
3
0 20
1 10
8 20
'''

'''
2
0 255
200 60
'''