import sys
sys.stdin.readline

#사각형 넓이
S  = 0
# 총 넓이
result  = 0

arr = [[0]*100 for _ in range(100)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1

for q in range(100):
    for w in range(100):
        if arr[q][w] == 1:
            result += 1
print(result)