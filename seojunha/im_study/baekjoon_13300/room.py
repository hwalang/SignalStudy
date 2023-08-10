import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

room = [0]*12
count = 0

for i in range(N):
    for k in range(1,7):
        if arr[i][1] == k and arr[i][0] == 0:
            room[k-1] += 1
        elif arr[i][1] == k and arr[i][0] == 1:
            room[(k-1)+6] += 1

for j in range(12):
    p = 0
    p = room[j] // K
    count += p
    if p*K != room[j] and room[j] != 0:
        count += 1


print(count)