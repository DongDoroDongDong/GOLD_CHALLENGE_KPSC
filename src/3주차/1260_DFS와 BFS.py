import sys
from collections import deque

input = sys.stdin.readline

def BFS(G, visit, v):
    q = deque()
    q.append(v)
    visit[v] = True
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for i in G[x]:
            if not visit[i]:
                visit[i] = True
                q.append(i)

def DFS_recursion(G, visit, v):
    visit[v] = True
    print(v, end = ' ')
    for i in G[v]:
        if not visit[i]:
            DFS_recursion(G, visit, i)
            
# DFS 스택 구현시, 스택에 집어넣는 행위 자체는 실제로 방문한 것이 아님
# 따라서 스택에서 뺄 때, 방문 검사와 방문 처리를 하면서 출력해야함 
# 기존에 정렬을 한 상태로 집어넣으면 작운 순서대로 방문이 아니라 역순으로 방문
# 따라서 집어넣을때도 입력받은 그래프를 뒤집어서 넣어줘야 목표하는 순서로 방문
def DFS_stack(G, visit, v):
    stack = [v]
    while stack:
        x = stack.pop()
        if not visit[x]:
            print(x, end = ' ')
            visit[x] = True
            for i in G[x][::-1]:
                stack.append(i)

n, m, v = map(int, input().split())
G = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in range(1, n+1):
    G[i].sort()
    
visit_DFS = [False] * (n+1)
visit_BFS = [False] * (n+1)

DFS_stack(G, visit_DFS, v)
# DFS_recursion(G, visit_DFS, v)
print()
BFS(G, visit_BFS, v)
    