T = int(input())

# 영역이 될 수 있는 K(반지름임)
Ks = []
for i in range(22):
    Ks.append(i + 1)

for tc in range(1, T+1):
    # 도시 변 크기, 지불 가격
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]

    # 중심이 될 수 있는 좌표
    center = []
    for i in range(N):
        for j in range(N):
            center.append([i, j])

    # 집들의 좌표
    home = []
    for i in range(N):
        for j in range(N):
            if town[i][j] == 1:
                home.append([i, j])


    # 최대 가구(찾고자 하는 답)
    max_home = 0

    # 중심 좌표 바꿔가면서
    for i in range(len(center)):
        temp = 0
        # 지원 영역 바꿔가면서
        for k in Ks:
            # 중심좌표, 지원 영역에 따라 들어가는 집의 수
            count = 0
            # 지원 영역에 들어가는 가구수 확인
            for h in range(len(home)):
                if abs(home[h][0] - center[i][0]) + abs(home[h][1] - center[i][1]) < k:
                    count += 1
                    if count == len(home):
                        break
            # 카운트를 다 찾았을 때, 손해가 아니면, temp 에 값 저장
            if (count * M) - ((k*k) + (k-1)*(k-1)) >= 0:
                temp = count
        if temp > max_home:
            max_home = temp

    print(f'#{tc} {max_home}')
