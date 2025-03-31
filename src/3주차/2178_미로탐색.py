import sys
from collections import deque

input = sys.stdin.readline

def BFS(G, visit, v):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    y, x = v[0], v[1]
    q = deque()
    q.append((y, x, 0))
    visit[y][x] = True
    while q:
        y, x, cnt = q.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if G[ny][nx] == '1' and not visit[ny][nx]:
                    visit[ny][nx] = True
                    q.append((ny, nx, cnt + 1))
                    
n, m = map(int, input().split())
G = []
for _ in range(n):
    G.append(list(input().strip()))
    
visit = [[False] * m for _ in range(n)]
print(BFS(G, visit, (0,0)))
