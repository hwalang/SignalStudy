# 색종이

T = int(input())
paper = [[0]*(101) for _ in range(1001)]

for tc in range(1, 1+T):
    y, x, m, n = map(int, input().split())


    for i in range(y, y+m):
        for j in range(x, x+n):
            paper[i][j] = tc

for j in range(T):
    cnt = 0
    for i in range(1001):
        cnt += paper[i].count(j+1)
# print(paper.count(2))

    print(cnt)    