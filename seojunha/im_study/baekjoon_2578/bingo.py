bingo = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]
counting = 0

for i in range(5):
    for j in range(5):
        for k in range(5):
            for p in range(5):
                if bingo[k][p] == numbers[i][j]:
                    bingo[k][p] = 0
                    counting += 1

                    if counting >= 12:  # 최소 12개의 숫자가 불렸을 때 빙고 여부를 확인
                        bingo_count = 0
                        for a in range(5):
                            count = 0
                            for b in range(5):
                                if bingo[a][b] == 0:
                                    count += 1
                                    if count == 5:
                                        bingo_count += 1

                        for c in range(5):
                            count = 0
                            for d in range(5):
                                if bingo[d][c] == 0:
                                    count += 1
                                    if count == 5:
                                        bingo_count += 1

                        if bingo[0][0] == bingo[1][1] == bingo[2][2] == bingo[3][3] == bingo[4][4] == 0:
                            bingo_count += 1
                        if bingo[0][4] == bingo[1][3] == bingo[2][2] == bingo[3][1] == bingo[4][0] == 0:
                            bingo_count += 1

                        if bingo_count >= 3:
                            print(counting)
                            exit()
