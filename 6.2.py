class Node:

    def __init__(self, data):

        self.data = data

        self.next = None

class Queue:

    def __init__(self):

        self.front = None

        self.rear = None

    def enqueue(self, x):

        new_node = Node(x)

        if self.rear is None:

            self.front = self.rear = new_node

        else:

            self.rear.next = new_node

            self.rear = new_node

        print(f"{x} inserted into the queue")

    def dequeue(self):

        if self.front is None:

            print("Queue underflow (Queue is empty)")

        else:

            x = self.front.data

            self.front = self.front.next

            if self.front is None:

                self.rear = None

            print(f"{x} deleted from the queue")

    def peek(self):

        if self.front is None:

            print("Queue is empty")

        else:

            print("Front element:", self.front.data)

    def display(self):

        if self.front is None:

            print("Queue is empty")

        else:

            print("The elements of the queue are:")

            current = self.front

            while current:

                print(current.data, end=" -> " if current.next else "")

                current = current.next

            print()  

if __name__ == "__main__":

    q = Queue()
 
    while True:

        print("\n--- Queue (Linked List) Operations Menu ---")

        print("1. Enqueue")

        print("2. Dequeue")

        print("3. Peek")

        print("4. Display")

        print("5. Exit")
 
        choice = input("Enter your choice (1-5): ")
 
        if choice == '1':

            val = int(input("Enter value to insert: "))

            q.enqueue(val)

        elif choice == '2':

            q.dequeue()

        elif choice == '3':

            q.peek()

        elif choice == '4':

            q.display()

        elif choice == '5':

            print("Exiting program.")

            break

        else:

            print("Invalid choice! Please enter a number between 1 and 5.")

 
