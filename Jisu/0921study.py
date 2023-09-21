# 백준 모든 순열

N = int(input())

def gen_permutation(n, depth, P):
    result = []
    if depth == n:
        
        return [P]
    else:
        for i in range(1, N+1):
            if chosen[i] == True:
                continue
            chosen[i] = True
            result += gen_permutation(n, depth+1, P+[i])
            chosen[i] = False
    return result


arr = [i for i in range(1, 1+N)]
chosen = [False for _ in range(N+1)]


result = gen_permutation(N, 0, [])
for i in range(len(result)):
    print(*result[i])