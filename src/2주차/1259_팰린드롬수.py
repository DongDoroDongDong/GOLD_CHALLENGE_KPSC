import sys

input = sys.stdin.readline

def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False
while True:
    n = input().strip()
    if n == '0':
        break
    if isPalindrome(n):
        print("yes")
    else:
        print("no")
    

    