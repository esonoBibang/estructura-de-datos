
class Node:

    'Creamos un clase nodo que contiene el valor  y el enlace'
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedLists:

    'Creamos una clase que genera la lista enlaza'
    def __init__(self):
        self.head = None #firs value of the linked list

    def insert_at_begining(self,data):
        node = Node(data,self.head) #creamos el objeto nodo con su valor
        self.head = node

    def print_linkedList(self):
        
        if self.head is None:
            print('My linked list is empty')
            return
            
        value = self.head

        LLstr = []#creamos un lista vacia en forma de un string
        while value:
            LLstr.append(value.data)
            #LLstr += str(value.data) + '-->' #agregamos el dato
            value = value.next #pasamos al siguiente dato

        print(LLstr)

    

#hacemos las llamadas
if __name__== '__main__':

    LL = LinkedLists() 
    
    LL.insert_at_begining(24)
    LL.insert_at_begining(20)
    LL.insert_at_begining(54)
    LL.insert_at_begining(17)
    LL.insert_at_begining(10)

    LL.print_linkedList()



