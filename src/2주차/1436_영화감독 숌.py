import sys

input = sys.stdin.readline

n = int(input())

if n < 7:
    print(1000*(n-1)+666)
else:
    temp = 6659
    cnt = 6
    while True:
        temp += 1
        if "666" in str(temp):
            cnt += 1
        if cnt == n:
            print(temp)
            break  
        