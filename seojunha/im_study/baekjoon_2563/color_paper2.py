import sys
input = sys.stdin.readline

t = int(input())
count = 0
arr = [[0]*100 for _ in range(100)]

for i in range(t):
    x1, y1 = map(int, input().split())
    for x in range(x1, x1+10):
        for y in range(y1, y1+10):
            arr[x][y] = 1

for p in range(100):
    for q in range(100):
        if arr[p][q] == 1:
            count += 1
print(count)