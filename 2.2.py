n= int(input("enter the no:of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))
arr.sort()
print("sorted:",arr)
key=int(input("enter the target:"))
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid=1
    return -1
print(binary_search(arr,key))
