import sys
from collections import deque

input = sys.stdin.readline

def BFS(v):
    q = deque()
    q.append((v,0))
    visit = set()
    while q:
        x, time = q.popleft()
        if x == k:
            return time
        
        x1 = x-1
        x2 = x+1
        x3 = x*2
        if 0 <= x1 <= 200000 and x1 not in visit:
            visit.add(x1)
            q.append((x1, time+1))
        if 0 <= x2 <= 200000 and x2 not in visit:
            visit.add(x2)
            q.append((x2, time+1))
        if 0 <= x3 <= 200000 and x3 not in visit:
            visit.add(x3)
            q.append((x3, time+1))
            

n, k = map(int, input().split())
print(BFS(n))