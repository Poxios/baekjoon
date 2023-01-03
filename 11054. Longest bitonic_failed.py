import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().rstrip().split()))
arr_max = max(arr)
answer = -sys.maxsize
for m in [idx for idx, v in enumerate(arr) if v == arr_max]:
    count_arr = [0]*n
    left_max = right_max = 0
    # 왼쪽으로
    for i in range(m-1, -1, -1):
        temp_max = 0
        for j in list(filter(lambda x: arr[x] > arr[i] and arr[x] != arr_max, list(range(i+1, m)))):
            temp_max = max(temp_max, count_arr[j])
        if arr[i] != arr_max:
            count_arr[i] = temp_max+1
        left_max = max(left_max, count_arr[i])
    # 오른쪽으로
    for i in range(m+1, n):
        temp_max = 0
        for j in list(filter(lambda x: arr[x] > arr[i] and arr[x] != arr_max, list(range(i-1, m, -1)))):
            temp_max = max(temp_max, count_arr[j])
        if arr[i] != arr_max:
            count_arr[i] = temp_max+1
        right_max = max(right_max, count_arr[i])

    answer = max(answer, left_max+right_max+1)
print(answer)
