n= int(input("enter no.of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    arr.append(int(input()))
key=int(input("enter the number:"))
def linear_search(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            print("element found at index:",i)
            return
    print("not found")
linear_search(arr,key)
