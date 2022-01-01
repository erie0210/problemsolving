import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)

n,m = map(int, sys.stdin.readline().split())
gph=[[] for _ in range(n+1)]
while m:
  m-=1
  u,v = map(int, sys.stdin.readline().split())
  gph[u].append(v)
  gph[v].append(u)

visit=[0 for _ in range(n+1)]

def dfs(num):
  if visit[num]==1:
    return
  visit[num]=1
  for i in gph[num]:
    dfs(i)
  return

count=0
for i in range(1, n+1):
  if visit[i]==0:
    count+=1
    dfs(i)
print(count)