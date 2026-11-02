def insertion_sort(arr):
    n=len(arr)
    for j in range(1,n):
        key=arr[j]
        j=j-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
n=int(input("enter the no:of elements"))
arr=[]
for i in range(n):
    x=int(input(f"enter the number(i+1):"))
    arr.append(x)
insertion_sort(arr)
print("sorted array:",arr)
