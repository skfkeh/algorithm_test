### BaekJoon
# https://www.acmicpc.net/problem/2511
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
ap, bp = 0, 0
nlist = []

for a, b in zip(alist, blist):
  if a > b:
    ap += 3
    nlist.append('A')
  elif a < b:
    bp += 3
    nlist.append('B')
  else:
    ap += 1
    bp += 1

print(ap, bp)
print('D') if alist==blist else print(nlist[-1]) if ap==bp else print('A') if ap>bp else print('B')
