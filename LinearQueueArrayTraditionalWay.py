###########################################################################################################################
#            # LINEAR QUEUE IMPLEMENTATION USING ARRAY IN PYTHON DSA (TRADITIONAL WAY) ##                                 #
# Linear Queue is a FIFO (First In First Out Data Structure.                                                              #
# This program demonstrates how the linear queue is implemented traditionally.                                            #
# The code length can be reduced using the append and pop built-in list methods.                                          #
# ------------------------------------------------------------------------------------------------------------------      #
#     The limitations of this approach are:                                                                               #
# 1. Fixed size of the queue.                                                                                             #
# 2. In case rear reaches Max-1 and front is not at 0 (greater than 0), even though there is available space, the queue   #
#     is full.                                                                                                            #
# 3. In such case, insertion is restart only after deleting all the elements.                                             #
#---------------------------------------------------------------------------------------------------------------------    #
#    Solutions:                                                                                                           #
# 1. Use append and pop built-in list methods to avoid building logic manually.                                           #
# 2. Using no MAX value removes the size limitation and the queue can store more data dynamically.                        #
# 3. Use Circular queue to avoid having to empty the queue if rear=MAX-1 and front > 0.                                   #
###########################################################################################################################

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
    
    
