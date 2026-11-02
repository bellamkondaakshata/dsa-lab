def quick_sort(a,low,high):
    if low<high:
        i=low
        j=high
        pivot=low
        while i<j:
            while i<len(a) and a[i]<=a[pivot]:
                i=i+1
            while a[j]>a[pivot]:
                j=j-1
            if i<j:
                a[i],a[j]=a[j],a[i]
        a[j],a[pivot]=a[pivot],a[j]
        quick_sort(a,low,j-1)
        quick_sort(a,j+1,high)
    return a
n=int(input("enter the no of elements:"))
a=[]
for i in range(n):
    x=int(input(f"enter the number(i+1):"))
    a.append(x)
quick_sort(a,0,n-1)
print("sorted array:",a)
