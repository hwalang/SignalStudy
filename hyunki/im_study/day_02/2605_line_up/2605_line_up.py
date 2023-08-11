import sys
sys.stdin = open('input.txt')

N = int(input())
number = list(map(int, input().split()))

students = []
for i in range(1,N+1):
    students.append(i)

line_up = []
for i in range(len(number)):
    line_up.insert(number[i],students[i])

line_up.reverse()

print(*line_up)
