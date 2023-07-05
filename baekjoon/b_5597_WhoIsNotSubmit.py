### BaekJoon
# https://www.acmicpc.net/problem/5597
nlist = [0]*30

while True:
  try:
    x = int(input())
    nlist[x-1] = 1
  except:
    break

for i in range(len(nlist)):
  if nlist[i] == 0:
    print(i+1, end=' ')
