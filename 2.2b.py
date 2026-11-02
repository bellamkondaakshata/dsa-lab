n= int(input("enter the no:of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))
key=int(input("enter the target:"))
if arr==sorted(arr):
    print("it is sorted")
else:
    print("array is not sorted")
    arr.sort()
    print("sorted array:",arr)
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return 'element found at index:', mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid=1
    return -1
print(binary_search(arr,key))
