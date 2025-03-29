import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in sorted(arr):
    print(*i)