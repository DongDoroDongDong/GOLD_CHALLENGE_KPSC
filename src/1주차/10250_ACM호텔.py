tc = int(input())
for _  in range(tc):
    h, w, n = map(int, input().split())
    stair = n % h
    number = 1 + n // h 
    if stair == 0:
        stair = h
        number -= 1
    print(100*stair + number)
    