import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

start = [0] * N
for i in range(N):
    start[i] = i + 1
# 시작 줄을 [1, 2, 3, 4, 5...]으로 만들었음

# 새로 만들 리스트
new_lst = []

# N번 뽑을 것임.
for j in range(N):
    # 새로운 인덱스 설정
    new_position = j - arr[j]
    # 새로운 인서트에 삽입
    new_lst.insert(new_position, start[j])

print(*new_lst)
