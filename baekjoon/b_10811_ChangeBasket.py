### BaekJoon
# https://www.acmicpc.net/problem/10811
def RvsNum(a, b, nlist):
  nlist[a:b+1] = list(reversed(nlist[a:b+1]))
  return nlist

n, m = map(int, input().split())
nlist = list(range(1, n+1))

for i in range(m):
  a, b = map(int, input().split())
  nlist = RvsNum(a-1, b-1, nlist)

for i in nlist:
  print(i, end=' ')
