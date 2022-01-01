import sys
sys.stdin = open('input.txt')

n,m = map(int,sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))

le = max(lis)
ri = 10000000000

def getTotal(lis, stdLength):
  sub_total=0
  cnt=1
  for minute in lis:
    if stdLength<sub_total+minute:
      cnt+=1
      sub_total=0
    sub_total+=minute
  return cnt


while le<=ri:
  mid = (le+ri)//2
  cnt = getTotal(lis, mid)
  if cnt==m:
    ri = mid-1
  if cnt>m:
    le = mid+1
  if cnt<m:
    ri = mid-1
print(le)
