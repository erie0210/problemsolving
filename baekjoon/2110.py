import sys
sys.stdin = open('input.txt')

n,c = map(int,sys.stdin.readline().split())
lis=[]
while n:
  n-=1
  lis.append(int(sys.stdin.readline().strip()))
n = len(lis)
lis = sorted(lis)

le = 1
ri = 100000000

def getCnt(lis, std):
  install=lis[0]
  cnt=1
  for i in range(1,n):
    if abs(lis[i]-install)>=std:
      cnt+=1
      install = lis[i]
  return cnt


while le<=ri:
  mid = (le+ri)//2
  cnt = getCnt(lis, mid)
  if cnt==c:
    le = mid+1
  if cnt>c:
    le = mid+1
  if cnt<c:
    ri = mid-1
print(ri)
