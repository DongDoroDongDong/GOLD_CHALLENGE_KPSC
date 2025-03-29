import sys

input = sys.stdin.readline

len_stack = 0
stack = []

for _ in range(int(input())):
    prompt = input().split()
    if prompt[0] == 'push':
        stack.append(prompt[1])
        len_stack += 1
    elif prompt[0] == 'top':
        print(stack[-1]) if stack else print(-1)
    elif prompt[0] == 'size':
        print(len_stack)
    elif prompt[0] == 'empty':
        print(1) if len_stack == 0 else print(0)
    elif prompt[0] == 'pop':
        print(stack.pop()) if stack else print(-1)
        if len_stack >= 1:
            len_stack -= 1