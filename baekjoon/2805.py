import sys
sys.stdin = open('input.txt')

n,m = map(int,sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))

sorted_lis = sorted(lis)

le = 0
ri = max(lis)+1

def getTotal(lis, height):
  total=0
  for tree in lis:
    if tree>height:
      total+=(tree-height)
  return total


while le<=ri:
  mid = (le+ri)//2
  total = getTotal(sorted_lis, mid)
  if total==m:
    le = mid+1
  if total>m:
    le = mid+1
  if total<m:
    ri = mid-1
print(ri)
