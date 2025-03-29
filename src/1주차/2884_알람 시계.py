a, b = map(int,input().split())

time = a*60 + b - 45
if time < 0:
    time = 1440 + time    
h, m = time//60, time%60
print(h, m)