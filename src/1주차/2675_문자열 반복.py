import sys
tc = int(input())
for _ in range(tc):
    n, x = input().split() 
    n = int(n)
    for i in x:
        print(i*n, end='')
    print()