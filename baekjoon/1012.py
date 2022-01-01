import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)

t = int(sys.stdin.readline())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def valid(r,c, n, m):
  return (r>=0 and c>=0 and r<n and c<m)

def dfs(r, c, visit, gph, n, m):
  if visit[r][c]==1:
    return
  visit[r][c]=1
  for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]
    if not valid(nr,nc, n, m):
      continue
    if gph[nr][nc]==0:
      continue
    if visit[nr][nc]==1:
      continue
    dfs(nr,nc, visit, gph, n, m)
  return

while t:
  t-=1

  m,n,k = map(int, sys.stdin.readline().split())
  gph=[[0 for _ in range(m)] for __ in range(n)]

  while k:
    k-=1
    c,r = map(int, sys.stdin.readline().split())
    gph[r][c] = 1

  visit = [[0 for _ in range(m)] for __ in range(n)]

  count=0
  for i in range(n):
    for j in range(m):
      if gph[i][j]==1 and visit[i][j]==0:
        count+=1
        dfs(i,j, visit, gph, n, m)
  print(count)