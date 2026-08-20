p=float(input("enter principal growth factor:"))
n=int(input("Enter num of year:"))
def power(p,n):
    if n==0:
        return 1
    else:
        return p*power(p,n-1)
result=power(p,n)
print("power=", result)
