# creating a queue from scratch

class Queue:
    def __init__(self):
        self.items = []

    def Enqueue(self,element):
        self.items.append(element)

    def Dequeue(self):
        if not len(self.items)==0:
            return self.items.pop(0)
        else:
            print("queue is empty")
    def is_empty(self):
        return len(self.items)==0

    def get_first_element(self):
        if not len(self.items)==0:
            return self.items[0]
        else:
            print("Queue is empty")

# create object/intance of class Queue
q = Queue()

# Enqueue elements
q.Enqueue(5)
q.Enqueue(10)
q.Enqueue(15)
q.Enqueue(20)

# Dequeue elements
print(q.Dequeue())

# Get the first element 
print(q.get_first_element())

# check whether queue is empty 
print(q.is_empty())

        
