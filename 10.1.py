size=10
table=[[] for i in range(size)]
def insert(key):
    index=key%size
    table[index].append(key)
def display():
    for i in range(size):
        print(i,":", table[i])
n=int(input("enter number of number:"))
for i in range(n):
    key=int(input("enter key:"))
    insert(key)
display()
