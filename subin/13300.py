# import sys
# sys.stdin = open('input2.txt')




N, K = map(int, input().split())  # 학생 수 N과 방 최대 인원수 K 입력
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))  # arr = 주어진 값을 행렬로



A=[]
for a1 in range(2):
    for a2 in range(1,7):
        A.append([a1,a2]) #A = [[0,1],[1,1],[0,2],[1,2],[0,3],[1,3],[0,4],[1,4],[0,5],[1,5],[0,6],[1,6]]]


B=[0]*12
for i in range(12):
    for j in arr:
        if A[i]==j:
            B[i]+=1 # B 는 12개로 분류한 정수값을 배열한 리스트


results=[]
for b in B:
    rooms= (b+K-1)//K       #   b=mK 인경우: m을 도출하고 싶다. 이때 (b+K-1)=Km+(K-1)이고 K로 나누면 몫은 m이다.
    results.append(rooms)  #  b=mK+r인경우(단, 0<r<K): m+1을 도출하고 싶다. (b+K-1)=K(m+1)+(r-1)이고 K로 나누면 몫이 m+1이다.
                            #즉, 문제가 없다.
print(sum(results))