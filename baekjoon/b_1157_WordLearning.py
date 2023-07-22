### Baekjoon
# https://www.acmicpc.net/problem/1157
import sys
alpha = [0]*26 # 알파벳 갯수(26)만큼 리스트화

txt = list(input().upper()) # 전체 대문자로 전환
for i in txt:
    alpha[ord(i)-65]+=1 # 나온 알파벳이 있으면 1 증가

print('?') if alpha.count(max(alpha))>1 else print(chr(alpha.index(max(alpha))+65))
