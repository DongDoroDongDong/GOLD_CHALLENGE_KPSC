import sys

input = sys.stdin.readline

n = int(input())
temp = 1
for i in range(1, n+1):
    temp *= i

temp = str(temp)[::-1]
i = 0 
while True:
    if temp[i] != '0':
        break
    i += 1
print(i)
    