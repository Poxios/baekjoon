from sys import stdin
input = stdin.readline

a = input()
b = input()
la = len(a)
lb = len(b)

if la < lb:
    for i in range(0, la):
        for j in range(i+1):
            substr = a[j:la-i+j]
            if b.find(substr) != -1:
                print(substr)
                exit(0)
else:
    for i in range(0, lb):
        for j in range(i+1):
            substr = a[j:lb-i+j]
            if b.find(substr) != -1:
                print(substr)
                exit(0)
