import sys
from collections import deque
import heapq

input = sys.stdin.readline

def BFS(G, visit, v):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    y, x = v[0], v[1]
    q = deque()
    q.append((y, x))
    visit[y][x] = True
    cnt = 1
    while q:
        y, x= q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if G[ny][nx] == '1' and not visit[ny][nx]:
                    visit[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1
    return cnt 
n = int(input())
G = []
for _ in range(n):
    G.append(list(input().strip()))

rst = []
visit = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if G[i][j] == '1' and not visit[i][j]:
            heapq.heappush(rst, BFS(G, visit, (i,j)))
            
print(len(rst))
while rst:
    print(heapq.heappop(rst))