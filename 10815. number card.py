input = __import__("sys").stdin.readline
input()
cards = set(input().rstrip().split())
input()
candidates = input().rstrip().split()
print(" ".join(["1" if x in cards else "0" for x in candidates]))
