def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter the num:"))
print(fib(n))
