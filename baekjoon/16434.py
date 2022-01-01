import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

N, Hatk = map(int, input().split())
lis = [list( map(int, input().split()) ) for _ in range(N) ]

le = 1
ri = int(2e17)

def play(life):
  max_life = life
  life = life
  attack = Hatk
  for turn in lis:
    [t, a, h] = turn
    if t==1:
      life-=(math.ceil(h/attack)-1)*a
      if life<1:
        return life
    else:
      attack += a
      life = min(life+h, max_life)
  return life


while le<=ri:
  mid = (le+ri)//2
  result = play(mid)
  if result<1:
    le = mid+1
  else :
    ri = mid-1
print(le)
