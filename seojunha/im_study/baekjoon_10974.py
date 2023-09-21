"""
모든 순열
1부터 N까지의 수로 이루어진 순열을 사전 순으로 출력하느 프로그램
"""
N = int(input())
lst = []
for i in range(1, N+1):
    lst.append(i)
visited = [False] * (N+1)

# 깊이, 현재 문자열
def dfs(depth, s):
    visited = [False] * (N + 1)
    for p in range(len(s)):
        if s[p] == ' ':
            continue
        else:
            visited[int(s[p])] = True
    if depth == N:
        print(s)
    else:
        for k in range(len(lst)):
            if visited[lst[k]] == False:
                visited[lst[k]] = True
                dfs(depth+1, s +" "+ str(lst[k]))



for i in range(N):
    dfs(1, str(lst[i]))
