p=float(input("enter principal growrh factor:"))
n=int(input("enter number of years:"))
def power(p,n):
    if n==0:
        return 1
    else:
        return p*power(p,n-1)
result=power(p,n)
print("power=",result)
