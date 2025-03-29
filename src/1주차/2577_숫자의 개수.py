a = int(input())
b = int(input())
c = int(input())
rst = str(a*b*c)
arr = [0] * 10
for i in list(rst):
    arr[int(i)] += 1
for i in arr:
    print(i)