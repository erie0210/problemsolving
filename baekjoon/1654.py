import sys
sys.stdin = open('input.txt')

K,N = map(int,sys.stdin.readline().split())
lis=[]
while K:
  K-=1
  lis.append(int(sys.stdin.readline().strip()))
K = len(lis)
lis = sorted(lis)

le = 1
ri = max(lis)

def getCnt(lis, std):
  cnt=0
  for stick in lis:
    cnt+=(stick//std)
  return cnt

while le<=ri:
  mid = (le+ri)//2
  cnt = getCnt(lis, mid)
  if cnt==N:
    le = mid+1
  if cnt>N:
    le = mid+1
  if cnt<N:
    ri = mid-1
print(ri)
