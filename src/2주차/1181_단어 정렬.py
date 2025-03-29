import sys
input = sys.stdin.readline

arr = set()
n = int(input())
for _ in range(n):
    arr.add(input().strip())

dict = {}
arr = list(arr)
for i in arr:
    if len(i) not in dict:
        dict[len(i)] = [i]
    else:
        dict[len(i)].append(i)

for i in sorted(dict.keys()):
    for j in sorted(dict[i]):
        print(j)    
