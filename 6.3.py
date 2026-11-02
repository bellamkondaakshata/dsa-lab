class CircularQueue:

    def __init__(self, size):

        self.size = size

        self.queue = [None] * size

        self.front = -1

        self.rear = -1

    def enqueue(self, x):

        if (self.rear + 1) % self.size == self.front:

            print("Queue overflow")

        else:

            if self.front == -1:  

                self.front = 0

                self.rear = 0

            else:

                self.rear = (self.rear + 1) % self.size

            self.queue[self.rear] = x

            print(f"{x} inserted into the queue")

    def dequeue(self):

        if self.front == -1:

            print("Queue underflow")

        else:

            x = self.queue[self.front]

            self.queue[self.front] = None

            if self.front == self.rear:

                self.front = -1

                self.rear = -1

            else:

                self.front = (self.front + 1) % self.size

            print(f"{x} deleted from the queue")

    def peek(self):

        if self.front == -1:

            print("Queue is empty")

        else:

            print("Front element:", self.queue[self.front])

    def display(self):

        if self.front == -1:

            print("Queue is empty")

        else:

            print("The elements of the queue are:")

            i = self.front

            while True:

                print(self.queue[i], end=" ")

                if i == self.rear:

                    break

                i = (i + 1) % self.size

            print()

if __name__ == "__main__":

    size = int(input("Enter the size of the circular queue: "))

    q = CircularQueue(size)

    while True:

        print("\n--- Circular Queue Operations Menu ---")

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

 
