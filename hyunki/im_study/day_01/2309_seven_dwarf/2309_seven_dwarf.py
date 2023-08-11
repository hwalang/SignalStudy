import sys
sys.stdin = open('input.txt')

# 난쟁이들 리스트에 집어넣기
dwarfs = []
for tc in range(9):
    a = int(input())
    dwarfs.append(a)

# 난쟁이 키 합
dwarfs_sum = sum(dwarfs)

# 두명의 난쟁이의 키를 뺀 값이 100이라면 잘못된 난쟁이 출력
for i in range(9):
    for j in range(1, 9):
        if dwarfs_sum - (dwarfs[i] + dwarfs[j]) == 100:
            worng1 = dwarfs[i]
            worng2 = dwarfs[j]

# 잘못된 난쟁이 2명 제거
dwarfs.remove(worng1)
dwarfs.remove(worng2)

# 오름차순 정렬
dwarfs.sort()

print(dwarfs)

