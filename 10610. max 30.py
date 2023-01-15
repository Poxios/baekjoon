arr = list(__import__('sys').stdin.readline().rstrip())
if sum(map(int, arr)) % 3 == 0:
    arr.sort(reverse=True)
    if arr[-1] == '0':
        print(''.join(arr))
        exit(0)
print('-1')
