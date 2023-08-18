import sys
sys.stdin = open('gg.txt')

def f(x, y, w, h):
    return {(i, j) for i in range(x, x + w) for j in range(y, y + h)}
def a(p):
    k = []
    for i in range(len(p)):
        # 현재 색종이의 영역
        cur = p[i]
        # 그 이후의 색종이들과의 교집합을 계산하여 합집합을 구하기 위한 초기 집합 설정
        ggg = set()
        for j in range(i + 1, len(p)):
            # 다음 색종이와의 겹치는 부분을 구해서 합집합에 추가
            ggg |= (cur & p[j])
        # 원래 영역에서 겹치는 영역을 빼서 최종적으로 보이는 영역 계산
        rrr = cur - ggg

        # 결과 리스트에 추가
        k.append(len(rrr))
    return k

# 입력 받기
N = int(input())
p = [f(*map(int, input().split())) for _ in range(N)] # *안쓰면 그냥 [1,2,3,4] 이런꼴임 함수에 넣기위해서는 1,2,3,4 꼴이어야 함


# 결과 출력
for b in a(p):
    print(b)










































