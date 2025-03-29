tc = int(input())
for _ in range(tc):
    temp = 0
    rst = 0 
    x = list(input())
    for i in x:
        if i == "O":
            temp += 1
            rst += temp
        else:
            temp = 0
    print(rst)