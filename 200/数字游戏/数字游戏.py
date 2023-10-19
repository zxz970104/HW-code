

def solve(nums, m, n):
    prefix_num = [0]
    total = 0
    for i in range(n):
        total += nums[i]
        prefix_num.append(total)
    
    for i in range(1, n+1):
        for j in range(i, n+1):
            tmp = prefix_num[j] - prefix_num[j-i]
            if tmp % m == 0:
                return 1
    
    return 0




while True:
    try:
        line = input()
        if not line:
            break
        n, m = [int(x) for x in line.split()]
        nums = [int(x) for x in input().split()]
        print(solve(nums, m, n))
    except:
        break
