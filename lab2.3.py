def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
n=int(input("enter the no.of elements:"))
arr=[]
for i in range(n):
    x=int(input(f"Enter the number{i+1}:"))
    arr.append(x)
selection_sort(arr)
print("sorted array:",arr)
