import sys
sys.stdin = open('ss.txt')

T = int(input())  # 테스트 케이스 수
# 테스트 케이스별로 실행
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 도시의 크기와 집당 비용
    city = [list(map(int, input().split())) for _ in range(N)]  # 도시 정보

    max_houses = 0  # 서비스 가능한 최대 집의 수

    # 가능한 모든 중심 위치를 순회
    for r in range(N):
        for c in range(N):
            for K in range(1, N + 2):  # 가능한 모든 K 값에 대해서
                houses = 0  # 현재 위치에서 서비스할 수 있는 집의 수
                cost = K * K + (K - 1) * (K - 1)  # 운영 비용

                # 마름모 영역 내의 모든 위치를 순회
                for dr in range(-K + 1, K):
                    for dc in range(-K + 1, K):
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < N and 0 <= new_c < N:
                            # |dr| + |dc| < K 인 경우에만 마름모 내부에 속함
                            if abs(dr) + abs(dc) < K:
                                houses += city[new_r][new_c]

                # 손해를 보지 않는 경우에만 최대값 갱신
                if houses * M >= cost:
                    max_houses = max(max_houses, houses)

    print(f"#{test_case} {max_houses}")












