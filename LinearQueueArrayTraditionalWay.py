## LINEAR QUEUE IMPLEMENTATION USING ARRAY IN PYTHON DSA (TRADITIONAL WAY) ##
class Queue:
    def __init__(self, MAX):
        self.MAX = MAX
        self.queue = []
        self.front = -1
        self.rear = -1
        
    def enqueue(self, data):
        if(self.rear < self.MAX-1):
            self.rear += 1
            self.queue.insert(self.rear, data)
            if(self.front == -1):
                self.front = 0
            print("Inserted: ", self.queue[self.rear])
        else:
            print("Queue is full.")
        
    def dequeue(self):
        if(self.front == -1):
            return None
        else:
            x = self.queue[self.front]
            if(self.front == self.rear):
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            return x
                
    def display(self):
        if(self.front == -1):
            return
        for i in range(self.front, self.rear+1):
            print(self.queue[i])
        
    def peek(self):
        if(self.front == -1):
            return None
        else:
            return self.queue[self.front]
 ################################################################################          
 
# menu function
def menu():
    print("-"*100)
    print("Linear Queue Implementation Using Array")
    print("Menu: 1. Enqueue 2. Dequeue 3. Display 4. Peek 0. Exit")
    choice = int(input("Enter choice: "))
    return choice
    
################################################################################
MAX = int(input("Enter size of queue: "))
Q = Queue(MAX)

while(True):
    choice = menu()
    if(choice == 1):
        data = int(input("Enter data: "))
        Q.enqueue(data)
    elif(choice == 2):
        data = Q.dequeue()
        if(data == None):
            print("Queue is empty.")
        else:
            print("Deleted: ",data)
    elif(choice == 3):
        print("Printing Queue: ")
        Q.display()
    elif(choice == 4):
        data = Q.peek()
        if(data == None):
            print("Queue is empty.")
        else:
            print("First element: ",data)
    elif(choice == 0):
        break
    else:
        print("Wrong choice.")
    choice = input("Enter any key to continue...")
print("Exited from program!")
##################################################################################
    
    
