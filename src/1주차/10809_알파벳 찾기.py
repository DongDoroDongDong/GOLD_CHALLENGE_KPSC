alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
idx = [-1] * 26
x = list(input())
for i in x:
    alpha_idx = alpha.index(i)
    if idx[alpha_idx] == -1:
        idx[alpha_idx] = x.index(i)
print(*idx)