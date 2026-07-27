
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
        if self.is_empty() == 1:
            return f"the stack list is empty, we can not remove"
        else:
            return f"{self._list.pop()} :The last item, removed" #remove and return the top item

    def peek(self):
        if self.is_empty() == 1:
            return f"Not items in to the Stack list"
        else:
            return self._list[-1] #view the top item without removing it

    def is_empty(self):
        if len(self._list) == 0:
            return 1
        else:
            return 0

    def __len__(self):
        return f"we have {len(self._list)}  items"

stack = STACK()
stack.push(23)
stack.push(14)
stack.push(34)
stack.push(67)

print(stack.__len__())
print(stack.pop())
print(stack.peek())
print(stack.__len__())