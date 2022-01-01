import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)

n,m,k = map(int, sys.stdin.readline().split())
gph = [[0 for _ in range(m)] for __ in range(n)]
visit = [[0 for _ in range(m)] for __ in range(n)]

def valid(r, c):
  return (r>=0 and c>=0 and r<n and c<m)

dr = [0,1,0,-1]
dc = [1,0,-1,0]


def dfs(r,c, size):
  visit[r][c]=size
  for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]
    if not valid(nr, nc):
      continue
    if visit[nr][nc]!=0:
      continue
    if gph[nr][nc]==0:
      continue
    visit[r][c] = dfs(nr, nc, visit[r][c]+1)
  return max(size, visit[r][c])

while k:
  k-=1
  r,c = map(int,sys.stdin.readline().split())
  gph[r-1][c-1]=1

max_size = -1000
for row in range(n):
  for col in range(m):
    if gph[row][col]==1 and visit[row][col]==0:
      size = dfs(row, col, 1)
      
      max_size = max(max_size, size)
print(max_size)