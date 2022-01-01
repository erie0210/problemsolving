import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
gph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visit = [[0 for _ in range(n+1)] for __ in range(n+1)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def valid(r, c):
  return r>=0 and c>=0 and r<n and c<n

def dfs(r,c, size):
  visit[r][c]=size
  for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]
    if not valid(nr,nc):
      continue
    if visit[nr][nc]!=0:
      continue
    if gph[nr][nc]==0:
      continue
    visit[r][c] = dfs(nr,nc,visit[r][c]+1)
  return visit[r][c]

count=0
ans=[]
for i in range(n):
  for j in range(n):
    if gph[i][j]==1 and visit[i][j]==0:
      count+=1
      result = dfs(i,j, 1)
      ans.append(result)
print(count)
ans = sorted(ans)
for a in ans:
  print(a)