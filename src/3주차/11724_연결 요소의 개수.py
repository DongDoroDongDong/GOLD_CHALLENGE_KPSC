import sys
from collections import deque

input = sys.stdin.readline

def BFS(G, visit, v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for nv in G[v]:
            if not visit[nv]:
                visit[nv] = True
                q.append(nv)
    

n, m = map(int, input().split())
G = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

rst = 0
visit = [False] * (n+1)
for i in range(1, n+1):
    if not visit[i]:
        rst += 1
        BFS(G, visit, i)
print(rst)