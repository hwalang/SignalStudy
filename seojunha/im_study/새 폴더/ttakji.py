aT = int(input())
for i in range(T):
    A = []
    B = []
    arr = [input().split() for _ in range(2)]
    A = (arr[0][1:])
    B = (arr[1][1:])


    if A.count('4') > B.count('4'):
        print('A')
    elif A.count('4') < B.count('4'):
        print('B')
    else:
        if A.count('3') > B.count('3'):
            print('A')
        elif A.count('3') < B.count('3'):
            print('B')
        else:
            if A.count('2') > B.count('2'):
                print('A')
            elif A.count('2') < B.count('2'):
                print('B')
            else:
                if A.count('1') > B.count('1'):
                    print('A')
                elif A.count('1') < B.count('1'):
                    print('B')
                else:
                    print('D')