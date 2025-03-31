import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def BFS(G, visit, v):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    y, x = v[0], v[1]
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if G[ny][nx] == 1 and not visit[ny][nx]:
                    visit[ny][nx] = True
                    q.append((ny,nx))

def DFS(G, visit, v):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    y, x = v[0], v[1]
    visit[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if G[ny][nx] == 1 and not visit[ny][nx]:
                DFS(G, visit, (ny, nx))
                
tc = int(input())
for _ in range(tc):
    m, n, k = map(int, input().split())
    G = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        G[y][x] = 1
    
    cnt = 0
    visit = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if G[i][j] == 1 and not visit[i][j]:
                cnt += 1
                DFS(G, visit, (i,j))
                # BFS(G, visit, (i,j))
    print(cnt)