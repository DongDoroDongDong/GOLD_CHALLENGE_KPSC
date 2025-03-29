rst, idx, temp = 0, 0, 0
for i in range(1, 10):
    x = int(input())
    temp = max(x ,temp)
    if rst != temp:
        rst, idx = temp, i
print(rst)
print(idx)