# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList():
    def __init__(self):
        self.head = None
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        

    def insert_after_node(self, previous_node, data):


      if not previous_node:
        print('P node is not there')
        return

      new_node = Node(data)
      new_node.next = previous_node.next
      previous_node.next = new_node

          


        
        
l = LinkedList()
l.append("A")
l.append("B")
l.append("C")

l.print_list() 
l.prepend("E")
print('------')
l.print_list()

l.insert_after_node(l.head.next.next, 'hello')

l.print_list()