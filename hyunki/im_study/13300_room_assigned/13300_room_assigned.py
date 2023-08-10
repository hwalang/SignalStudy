import sys
sys.stdin = open('input2.txt')

N, max_room = map(int, input().split())
# 여자 남자 리스트에 학년별로 값이 들어오게 0으로 된 리스트 생성
students = [[0,0,0,0,0,0], [0,0,0,0,0,0]]

for i in range(N):
    gender, grade = list(map(int, input().split()))
    students[gender][grade-1] += 1  # 0이면 왼쪽,1이면 오른쪽에 학년별로 인원수 1씩 증가

    need_room = 0

    for i in students:
        for grade_num in i:
            if grade_num % max_room == 0:
                need_room += (grade_num // max_room)
            else:
                need_room += grade_num // max_room + 1

print(need_room)