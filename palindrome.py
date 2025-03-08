n=int(input())
n_re=int(str(n)[::-1])
if (n_re == n):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
