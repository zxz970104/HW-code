n,m,k = [int(x) for x in input().split()]
ct_idx = set([int(x) for x in input().split()])
ability = [int(x) for x in input().split()]
count = 0
for i in range(n):
    if i in ct_idx:
        continue
    for j in ct_idx:
        if j > i:
            continue
        if ability[j] > ability[i]:
            count += 1
print(count)
print(1 if count > k else 0)

'''
4 2 3
0 1
10 9 1 2
'''