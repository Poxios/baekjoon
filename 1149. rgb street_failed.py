import sys
input = sys.stdin.readline
n = int(input())

board = [list(map(int, input().rstrip().split())) for _ in range(n)]
temp = board[0]
min_index = min(range(len(temp)), key=temp.__getitem__)
prev_color = min_index
answer = temp[min_index]

for cursor in range(1, len(board)):
    row = board[cursor]
    target_index = min(
        [(prev_color+x+1) % 3 for x in range(2)], key=row.__getitem__)
    answer += row[target_index]
    print(row[target_index])
    prev_color = target_index


print(answer)
