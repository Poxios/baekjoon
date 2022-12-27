import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for i in range(T):
    func = list(input().strip())
    input()
    Q = deque()
    if (raw := input().strip()) != '[]':
        Q = deque(list(map(int, raw[1:-1].split(','))))
    is_reversed = False
    is_error = False
    for f in func:
        if f == 'R':
            is_reversed = not is_reversed
        else:  # D
            if len(Q) == 0:
                is_error = True
                break
            Q.pop() if is_reversed else Q.popleft()
    Q = list(Q)
    print('error' if is_error else str(Q[::-1] if is_reversed else Q).replace(' ', ''))
    # OUTPUT.append('error' if is_error else str(Q[::-1] if is_reversed else Q).replace(' ', ''))
