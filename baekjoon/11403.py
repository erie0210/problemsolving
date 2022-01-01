from __future__ import print_function
import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)


n = int(sys.stdin.readline())

gph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for __ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if gph[i][k] and gph[k][j]:
        gph[i][j] = 1

for row in gph:
  for col in row:
    print(col, end = ' ')
  print()