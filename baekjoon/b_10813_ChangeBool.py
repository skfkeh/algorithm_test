### BaekJoon
# https://www.acmicpc.net/problem/10813
def chgNum(a, b, nlist):
  nlist[a], nlist[b] = nlist[b], nlist[a]

n, m = map(int, input().split())
nlist = list(range(1, n+1))

for i in range(m):
  a, b = map(int, input().split())
  chgNum(a-1, b-1, nlist)
  # print(nlist)

for i in nlist:
  print(i, end=' ')
