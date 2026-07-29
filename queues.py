#A queue is a linear data structure that follows the FIFO principle: First In, First Out. Imagine a line of
#people waiting to buy tickets — the first person to join the line is the first one served.

#Core operations of a queue include:
#1. Enqueue (insert): Adding an element to the end of the queue.
#2. Dequeue (pop): Removing an element from the front of the queue.
#3. Peek/Front: Viewing the element at the front of the queue without removing it.
#4. IsEmpty: Checking if the queue is empty.

from collections import deque

class Queue:

    def __init__(self):
        self._item = deque() #(initialize an empty deque to store queue items)

    def enqueue(self, item):
        self._item.append(item) # (add to at back of queue)

    #dequeue method removes and returns the front item of the queue. If the queue is empty, 
    # it returns a message indicating that the queue is empty and cannot dequeue.
    def dequeue(self):
        if not self.is_empty():
            return f"this is the first item removed: {self._item.popleft()}" # (remove from front)
        else:
            return "Queue is empty, cannot dequeue."
        
    #checks if the queue is empty and returns a message indicating that the queue is empty and cannot view the front item.
    def front(self):
        if not self.is_empty():
            return f"Front item: {self._item[0]}" # (return front item)
        else:
            return "Queue is empty, cannot view front item."

    #checks if the queue is empty and returns a boolean value indicating whether the queue is empty or not.
    def is_empty(self):
        return len(self._item) == 0 # (check if empty)

    def last(self):
        if not self.is_empty():
            return f"Last item: {self._item[-1]}" # (return last item)
        else:
            return "Queue is empty, cannot view last item."

    def print_queue(self):
        print(self._item) # (print the current state of the queue)

fila = Queue() # (create a new queue instance)

fila.enqueue("ANTONIO") # (add "ANTONIO" to the queue)
fila.enqueue("MARIA") # (add "MARIA" to the queue)
fila.enqueue("JOAO") # (add "JOAO" to the queue)
fila.enqueue("PEDRO") # (add "PEDRO" to the queue)
fila.enqueue("LUCAS") # (add "LUCAS" to the queue)

fila.print_queue() # (print the current state of the queue)
fila.dequeue()
fila.print_queue() # (print the current state of the queue after dequeue)
print(fila.front()) # (print the front item of the queue)
print(fila.last()) # (print the last item of the queue)