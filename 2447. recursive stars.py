n = int(input())

board = [[' ']*n for _ in range(n)]


def recur(n, p, q):
    global board
    if n == 1:
        board[p][q] = '*'
        return
    divided = n//3

    recur(divided, p, q)
    recur(divided, p+divided, q)
    recur(divided, p, q+divided)
    recur(divided, p+2*divided, q+divided)
    recur(divided, p+divided, q+2*divided)
    recur(divided, p, q+2*divided)
    recur(divided, p+2*divided, q)
    recur(divided, p+2*divided, q+2*divided)


recur(n, 0, 0)

print('\n'.join([''.join(x) for x in board]))
