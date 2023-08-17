import sys
sys.stdin = open('input0809study.txt')

def generate_pascal_subset(N):
    list_storage = list(range(1, N + 1)) + list(range(N, 0, -1))
    pascal_subset = []

    for i in range(1 << len(list_storage)):
        subset = []
        for j in range(len(list_storage)):
            if i & (1 << j):
                subset.append(list_storage[j])

        for k in range(N):        
            if sum(subset) == 2 ** k and subset == subset[::-1] and subset[0] == 1 and len(subset) == k+1:
                pascal_subset.append(subset)

    result = []
    for value in pascal_subset:
        if value not in result:
            result.append(value)
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    
    pascal_subset = generate_pascal_subset(N)
    print(f'#{tc}')
    for subset in pascal_subset:
        print(*subset)
