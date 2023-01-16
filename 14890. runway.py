from sys import stdin
input = stdin.readline
n, l = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]
answer = 0
for row in range(n):
    failed = False
    for idx in range(n-1):
        if (a := matrix[row][idx]) != (b := matrix[row][idx+1]):
            if abs(a-b) != 1:
                failed = True
                break
            elif a > b:  # 앞이 높음. 뒤에다 경사 놔야함.
                if idx+l < n and matrix[row][idx+l] == a-1:
                    pass
                else:
                    failed = True
                    break
            else:  # 뒤가 더 높다. 앞에 경사 놔야함.
                if idx-l >= 0 and matrix[row][idx-l] == b-1:
                    pass
                else:
                    failed = True
                    break
    if not failed:  # 한줄 다 돌았는데 실패가 아니다.
        print('dd', row)
        answer += 1

print(answer)
