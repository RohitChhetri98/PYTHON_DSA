###########################################################################################################################
#            # LINEAR QUEUE IMPLEMENTATION USING ARRAY IN PYTHON DSA (PYTHON WAY) ##                                      #
# Linear Queue is a FIFO (First In First Out Data Structure.                                                              #
# This program demonstrates how the linear queue is implemented in Python Way.                                            #
# The code length has been reduced using the append and pop built-in list methods.                                        #
###########################################################################################################################
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        return self.queue.pop(0)
                
    def display(self):
        print(self.queue)
        
    def peek(self):
        return self.queue[0]
 ################################################################################          
 
# menu function
def menu():
    print("-"*100)
    print("Linear Queue Implementation Using Array")
    print("Menu: 1. Enqueue 2. Dequeue 3. Display 4. Peek 0. Exit")
    choice = int(input("Enter choice: "))
    return choice
    
################################################################################
Q = Queue()

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
    
    
