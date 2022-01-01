import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)

t = int(sys.stdin.readline())

def dfs(num, visit, lis, teamCount, curVisit):
  # print('idx', num)
  if num in curVisit:
    # print("circle")
    return teamCount-curVisit[num]
  if visit[num]==1:
    # print("already visited")
    return 0
  visit[num]=1
  if lis[num]==num+1:
    # print("self")
    return 1
  curVisit[num]=teamCount
  return dfs(lis[num]-1, visit, lis, teamCount+1, curVisit)

while t:
  t-=1
  n = int(sys.stdin.readline())
  lis = list(map(int, sys.stdin.readline().split()))
  visit = [0 for _ in range(len(lis)+1)]

  count=0
  for idx in range(len(lis)):
    if visit[idx]==0:
      curVisit={}
      result = dfs(idx, visit, lis, 1, curVisit)
      # print("result", result)
      count+=result
    # else: 
    #   print("skip", idx)
  print(len(lis)-count)