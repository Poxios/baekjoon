import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
print('\n'.join([' '.join(map(str, x))
      for x in permutations(range(1, n+1), m)]))
