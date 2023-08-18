import sys
sys.stdin = open('ff.txt')

def f(x, y):
    return {(i, j) for i in range(x, x + 10) for j in range(y, y + 10)}


N = int(input())
p = [f(*map(int, input().split())) for _ in range(N)] # *안쓰면 그냥 [1,2] 이런꼴임 함수에 넣기위해서는 1,2 꼴이어야 함


u = set()
for s in p:
    u |= s

print(len(u))

