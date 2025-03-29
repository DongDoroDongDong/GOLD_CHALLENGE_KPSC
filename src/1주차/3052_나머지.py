dict = {}
for _ in range(10):
    n = int(input())
    n %= 42
    if n not in dict:
        dict[n] = 1 
    else:
        dict[n] += 1
print(len(dict.keys()))