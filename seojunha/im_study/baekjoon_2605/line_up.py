import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]

n = len(arr)
result = []
for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(arr[j])
        if len(subset) == 7 and sum(subset) == 100:
            result = sorted(subset)

for x in result:
    print(x)
