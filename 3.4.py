def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1
    while i<len(left):
        arr[k]=left[i]
        i=i+1
        k=k+1
    while j<len(right):
        arr[k]=right[j]
        j=j+1
        k=j+1
n=int(input(f"enter no of elements:"))
arr=[]
for i in range(n):
    x=int(input(f"enter the number(i+1):"))
    arr.append(x)
merge_sort(arr)
print("sorted array:",arr)
        
