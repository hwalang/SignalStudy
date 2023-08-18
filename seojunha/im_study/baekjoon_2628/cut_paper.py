import sys
input = sys.stdin.readline

# 가로, 세로
N, M = map(int, input().split())
T = int(input())

lst1 = [0]
lst2 = [0]

# T번의 작업을 수행
for _ in range(T):
    x, y = map(int, input().split())

    if x == 0:
        lst1.append(y)
    if x == 1:
        lst2.append(y)

lst1.sort()
lst2.sort()

lst1.append(M)
lst2.append(N)

max_h = 0
for i in range(len(lst1)-1):
    if max_h < lst1[i+1]-lst1[i]:
        max_h = lst1[i+1]-lst1[i]


max_w = 0
for j in range(len(lst2)-1):
    if max_w < lst2[j+1]-lst2[j]:
        max_w = lst2[j+1]-lst2[j]

result = max_h * max_w

print(result)