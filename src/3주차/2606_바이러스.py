import sys
from collections import deque

input = sys.stdin.readline

def BFS(G, v):
    q = deque()
    q.append(v)
    visit = [False] * (n+1)
    visit[v] = True
    cnt = 0 
    while q:
        v = q.popleft()
        for nv in G[v]:
            if not visit[nv]:
                visit[nv] = True
                q.append(nv)
                cnt += 1
    return cnt
    
def DFS(G, visit, v):
    cnt = 1
    visit[v] = True
    for nv in G[v]:
        if not visit[nv]:
            cnt += DFS(G, visit, nv)
    return cnt
        

n = int(input())
m = int(input())

G = [[]for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
visit = [False] * (n+1)
# print(BFS(G, 1))
print(DFS(G, visit, 1) - 1)
    