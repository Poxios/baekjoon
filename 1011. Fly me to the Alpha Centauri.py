import math

count = int(input())
board = [list(map(int, input().split())) for _ in range(count)]
d_list = [x[1]-x[0] for x in board]
for d in d_list:
    sqrted = math.sqrt(d)
    floored = math.floor(sqrted)
    if sqrted.is_integer():
        print(2*int(sqrted)-1)
    elif d <= floored**2+floored:
        print(2*floored)
    else:
        print(2*floored+1)
