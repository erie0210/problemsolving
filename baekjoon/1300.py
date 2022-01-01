import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

le = 1
ri = N*N

def getCount(limit):
  count=0
  for i in range(1, N+1):
    count+=(min(limit//i, N))
  return count

while le<=ri:
  mid = (le+ri)//2
  result = getCount(mid)
  if result==k:
    ri = mid-1
  if result<k:
    le = mid+1
  elif result>k:
    ri = mid-1
print(le)