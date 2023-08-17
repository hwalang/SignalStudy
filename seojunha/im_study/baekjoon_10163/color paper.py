import sys
input = sys.stdin.readline

N = int(input())

arr = [[0] * 1001 for _ in range(1001)]

s = []

for i in range(N):
    x1, y1, w, h = map(int, input().split())

    s.append((x1, y1, x1+w, y1+h))

for j in range(N):
    for x in range(s[j][0], s[j][2]):
        for y in range(s[j][1], s[j][3]):
            arr[x][y] = j+1

target = 1

for q in range(N):
    count = 0
    for k in range(1001):
        for p in range(1001):
            if arr[k][p] == target:
                count += 1
    target+=1
    print(count)