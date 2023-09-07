import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

# 섬의 개수를 세자
# 1은 땅, 0은 바다
# 대각선으로 연결되어 있어도 섬 1개

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]


def island(x, y):
     arr[x][y] = 0  # 지금 있는 곳 0으로 만들어 주기
     for k in range(8):
         nx = x + dx[k]
         ny = y + dy[k]

         if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
             island(nx, ny)


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    count = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                island(i, j)
                count += 1

    print(count)



