
#A stack is a linear data structure that follows the LIFO principle: Last In, First Out.

#Operations:
#       push(item)
#       pop()
#       peek()/top()
#       is_empty()

class STACK:
    def __init__(self):
        self._list = []

    def push(self,item):
        self._list.append(item)

    def pop(self):
        if self.is_empty():
            raise f"the list is empty"
        return self._list.pop() #remove and return the top item

    def peek(self):
        if self.is_empty():
            raise f"Not items in to the list"
        return self._list[-1] #view the top item without removing it

    def is_empty(self):
        return self._list == 0

    def __len__(self):
        return len(self._list)

stack = STACK()
stack.push(12)
stack.push(2)
stack.push(42)
stack.push(13)
stack.push(19)
print(stack.peek())