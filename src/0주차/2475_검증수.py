arr = list(map(int, input().split()))
rst = 0
for i in arr:
    rst += (i**2) % 10
print(rst%10)