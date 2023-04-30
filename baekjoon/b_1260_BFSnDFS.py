### BAEKJOON
# https://www.acmicpc.net/problem/1260
from collections import deque

def bfs(graph, root):
    visited = []
    queue = deque([root])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort()
                queue += tmp
    return " ".join(str(i) for i in visited)
    
def dfs(graph, root):
    visited = []
    stack = [root]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                tmp = list(set(graph[n]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp
    return " ".join(str(i) for i in visited)

graph = {}
n, m, v = map(int, input().split())

for i in range(m):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
        
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
        
print(dfs(graph, v))
print(bfs(graph, v))
