import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())


sorted_li = sorted(li)

le = 0
ri = max(li)

def getTotal(lis, std):
  total=0
  for money in lis:
    total+=min(money,std)
  return total


while le<=ri:
  mid = (le+ri)//2
  total = getTotal(sorted_li, mid)
  if total<=M:
    le = mid+1
  if total>M:
    ri = mid-1
print(ri)
