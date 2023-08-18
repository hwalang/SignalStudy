import sys
sys.stdin = open('ff.txt')

w, h = map(int, input().split())
N = int(input())

a,b = [0,h],[0,w]

for _ in range(N):
    c,d  = map(int, input().split())
    if c == 0:
        a.append(d)
    else:
        b.append(d)

# 각 리스트를 정렬합니다.
a.sort()
b.sort()

# 가로와 세로의 최대 간격을 찾습니다.
mx1 = max([a[i+1] - a[i] for i in range(len(a)-1)])
mx2 = max([b[i+1] - b[i] for i in range(len(b)-1)])

# 가장 큰 종이 조각의 넓이를 출력합니다.
print(mx1*mx2)

