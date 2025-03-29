import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
max_v = max(arr)
for i in range(n):
    arr[i] = arr[i]/max_v * 100
print(sum(arr)/n)