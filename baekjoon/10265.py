import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)

n,k = map(int,sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))
gph = [[] for __ in range(n)]

for i in range(n):
  num1 = i
  num2 = lis[i]-1
  gph[num1].append(num2)
  gph[num2].append(num1)

visit = [0 for _ in range(n)]

def dfs(num, size):
  visit[num]= size
  for n in gph[num]:
    if visit[n]!=0:
      continue
    visit[num]=dfs(n, visit[num]+1)
  return visit[num]

answer=[]
for i in range(n):
  if visit[i]==0:
    result = dfs(i, 1)
    answer.append(result)
answer = sorted(answer)
# print(answer)

ans=0
for num in answer:
  if k>=num:
    k-=num
    ans+=num
print(ans)
