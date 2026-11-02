size = 10
table=[-1]*size
def insert(key):
    index=key%size
    i=0
    while i<size:
        new_index=(index+i*i)%size
        if table[new_index]==-1:
            table[new_index]=key
            return
        i+=1
    print("hash table is full or no slot found")
def display():
    for i in range(size):
        print(i,"i", table[i])
n=int(input("enter no of elements:"))
for i in range(n):
    key=int(input("enter key:"))
    insert(key)

display()
