import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board += list(input().rstrip())

visited = [0] * (n*n)
w_visited = [0] * (n*n)

Q = deque([0])
last_char = ''
last_idx = -1

total_cnt, weak_cnt = 0, 0


def chk_same_before(a, b):
    if (a == 'R' or a == 'G') and (b == 'R' or b == 'G'):
        return True
    elif (a == 'B' and b == 'B'):
        return True
    return False


while Q:
    curr_idx = Q.pop()
    curr_char = board[curr_idx]
    # 만약 이전이랑 다르면, 카운트 + 1함
    if not chk_same_before(curr_char, last_char):
        if last_char != '':
            total_cnt += 1
        # 심지어 이전이 적록이었으면 원래 구역이 몇개였는지 체크하고 temp에 저장
        if last_char == 'R' or last_char == 'G':
            temp = 0
            wQ = deque([last_idx])
            w_last_char = ''
            # 여기서 다시 체크
            while wQ:
                w_curr_idx = wQ.pop()
                w_curr_char = board[w_curr_idx]
                if w_last_char != w_curr_char:
                    temp += 1
                w_last_char, w_last_idx = w_curr_char, w_curr_idx
                w_avail_pos = []
                # up
                if (p := w_curr_idx-n) >= 0 and w_visited[p] == 0 and board[p] != 'B':
                    w_avail_pos.append(p)
                # right
                if (p := w_curr_idx+1) < n*n and w_visited[p] == 0 and board[p] != 'B':
                    w_avail_pos.append(p)
                # down
                if (p := w_curr_idx+n) < n*n and w_visited[p] == 0 and board[p] != 'B':
                    w_avail_pos.append(p)
                # left
                if (p := w_curr_idx-1) >= 0 and w_visited[p] == 0 and board[p] != 'B':
                    w_avail_pos.append(p)
                for v in w_avail_pos:
                    if board[v] == w_curr_char:
                        wQ.append(v)
                    else:
                        wQ.appendleft(v)
                    w_visited[v] = 1
            weak_cnt += temp
        elif last_char == 'B':
            weak_cnt += 1
    last_char, last_idx = curr_char, curr_idx
    avail_pos = []
    # 4방향이 벽이 아니고 이전에 방문한 곳이 아니면
    # up
    if curr_idx-n >= 0 and visited[curr_idx-n] == 0:
        avail_pos.append(curr_idx-n)
    # right
    if curr_idx+1 < n*n and visited[curr_idx+1] == 0:
        avail_pos.append(curr_idx+1)
    # down
    if curr_idx+n < n*n and visited[curr_idx+n] == 0:
        avail_pos.append(curr_idx+n)
    # left
    if curr_idx-1 >= 0 and visited[curr_idx-1] == 0:
        avail_pos.append(curr_idx-1)

    for v in avail_pos:
        # 지금이랑 같은 색이면 큐 오른쪽 추가
        if chk_same_before(curr_char, board[v]):
            Q.append(v)
        # 다르면 왼쪽 추가
        else:
            Q.appendleft(v)
        visited[v] = 1

# 다 끝났는데 마지막 색이 RG면 다시 돌리기
if last_char == 'R' or last_char == 'G':
    temp = 0
    wQ = deque([last_idx])
    w_last_char = ''
    # 여기서 다시 체크
    while wQ:
        w_curr_idx = wQ.pop()
        w_curr_char = board[w_curr_idx]
        if w_last_char != w_curr_char:
            temp += 1
        w_last_char, w_last_idx = w_curr_char, w_curr_idx
        w_avail_pos = []
        # up
        if (p := w_curr_idx-n) >= 0 and w_visited[p] == 0 and board[p] != 'B':
            w_avail_pos.append(p)
        # right
        if (p := w_curr_idx+1) < n*n and w_visited[p] == 0 and board[p] != 'B':
            w_avail_pos.append(p)
        # down
        if (p := w_curr_idx+n) < n*n and w_visited[p] == 0 and board[p] != 'B':
            w_avail_pos.append(p)
        # left
        if (p := w_curr_idx-1) >= 0 and w_visited[p] == 0 and board[p] != 'B':
            w_avail_pos.append(p)
        for v in w_avail_pos:
            if board[v] == w_curr_char:
                wQ.append(v)
            else:
                wQ.appendleft(v)
            w_visited[v] = 1
    weak_cnt += temp
    print(f'{weak_cnt} {total_cnt+1}')
else:
    print(f'{weak_cnt+1} {total_cnt+1}')
