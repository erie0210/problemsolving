import sys
sys.stdin = open('input.txt')

n,k,d = map(int,sys.stdin.readline().split())
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

le = 1
ri = n

def getCount(limit):
  count=0
  for rule in lis:
    [s, e, diff] = rule
    e = min(e,limit)
    if s<=e:
      count+=((e-s)//diff)+1
  return count

while le<=ri:
  mid = (le+ri)//2
  result = getCount(mid)
  if result<d:
    le = mid+1
  if result>d:
    ri = mid-1
  if result==d:
    ri = mid-1
print(le)