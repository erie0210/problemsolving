import sys
sys.stdin=open('input.txt')
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
gph = [list(sys.stdin.readline().strip()) for _ in range(n)]
visit = [[0 for _ in range(n)] for __ in range(n)]
visit_blind = [[0 for _ in range(n)] for __ in range(n)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def valid (row, col):
  return(row>=0 and col>=0 and row<n and col<n)

def dfs_blind(row, col, visit_blind):
  visit_blind[row][col]=1
  for i in range(4):
    nr = row+dr[i]
    nc = col+dc[i]
    if not valid(nr, nc):
      continue
    if visit_blind[nr][nc]!=0:
      continue
    if gph[row][col]=='B':
      if gph[nr][nc]=='B':
        dfs_blind(nr, nc, visit_blind)
    else:
      if gph[nr][nc]!='B':
        if gph[nr][nc]!='B':
          dfs_blind(nr, nc, visit_blind)
  return


def dfs(row, col, visit):
  visit[row][col]=1
  for i in range(4):
    nr = row+dr[i]
    nc = col+dc[i]
    if not valid(nr, nc):
      continue
    if visit[nr][nc]!=0:
      continue
    if gph[row][col] == gph[nr][nc]:
      dfs(nr, nc, visit)
  return

count=0
for i in range(n):
  for j in range(n):
    if visit[i][j]==0:
      count+=1
      dfs(i,j, visit)
print(count)

count=0
for i in range(n):
  for j in range(n):
    if visit_blind[i][j]==0:
      count+=1
      dfs_blind(i,j, visit_blind)
print(count)
