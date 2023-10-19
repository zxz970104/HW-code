

def solve(nums, m, n):

    remain = set()  # 不可以写成set(0)
    remain.add(0)

    total = 0
    for i in range(n):
        total += nums[i]

        if total % m in remain:
            return 1
        else:
            remain.add(total % m)
    return 0




while True:
    try:
        line = input()
        if not line:
            break
        n, m = [int(x) for x in line.split()]
        nums = [int(x) for x in input().split()]
        print(nums, m, n)
        print(solve(nums, m, n))
    except:
        break
