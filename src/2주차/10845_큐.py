import sys

input = sys.stdin.readline

len_q = 0
q = []

for _ in range(int(input())):
    prompt = input().split()
    if prompt[0] == 'push':
        q.append(prompt[1])
        len_q += 1
    elif prompt[0] == 'pop':
        if len_q > 0:
            temp = q[0]
            for i in range(len_q - 1):
                q[i] = q[i+1]
            len_q -= 1
            q.pop()
            print(temp)
        else:
            print(-1)
    elif prompt[0] == 'size':
        print(len_q)
    elif prompt[0] == 'empty':
        print(1) if len_q == 0 else print(0)
    elif prompt[0] == 'front':
        print(q[0]) if len_q != 0 else print(-1)
    elif prompt[0] == 'back':
        print(q[-1]) if len_q != 0 else print(-1)

