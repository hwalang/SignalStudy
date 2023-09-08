from collections import deque
import sys
sys.stdin = open('input.txt')

# 걸어가면 X+1 or X-1, 순간이동 하면 2*X
# 수빈이 위치에서 시작
# 빈 배열에 수빈이가 갈수 있는 X-1,X+1,X*2 위치에 전부 +1 해놓기
# 큐를 순회하면서 빈 배열에 갈수 있는 곳에 전부 값 집어넣기
# 동생이 있는 위치에 도달하게 되면 리턴


def bfs(N):
    q = deque()
    q.append(N)
    while q:
        move = q.popleft()
        if move == M:
            return arr[move]
        for next_move in (move - 1, move + 1, move * 2):
            if 0 <= next_move < MAX and arr[next_move] == 0:
                arr[next_move] = arr[move] + 1
                q.append(next_move)


N, M = map(int, input().split())
MAX = 100001
arr = [0] * MAX

print(bfs(N))