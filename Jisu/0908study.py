# 백준 실1 숨박꼭질

start, end = map(int, input().split())

queue = [[start]] # 시작
cnt = 0 # 초
switch = 1 
while switch == 1:
    cnt += 1 # 1초가 지남
    node = queue.pop(0) # 큐 처음값이 노드임
    # print(node)
    queue2 = [] # 임시 큐
    for i in node: # 노드 리스트 처음부터 계산
        if i+1 == end or i-1 == end or 2*i == end:
            print(cnt)
            switch = 0
            break
        else:
            queue2.append(i+1) 
            queue2.append(i-1)
            queue2.append(2*i)
        
    queue.append(queue2)

