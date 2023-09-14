# 그니까 트리 구조 생각해 봐야됨

#         1
#      4       6
#    2   7   3
#          5  
from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
Trees = [list(map(int, input().split())) for _ in range(N-1)]

# cnt2 = 2
# while cnt2 != N+1:
while 1:
    for i in range(2,N+1):
        cnt = 0

        for node1, node2 in Trees:
            cnt += 1

            if i == node1:
                print(node2)
                # cnt2 += 1
                Trees.pop(cnt-1)
                break 
            
            elif i == node2:
                print(node1)
                # cnt2 += 1
                Trees.pop(cnt-1)
                break
    quit()
        
