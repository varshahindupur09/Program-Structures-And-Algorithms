class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getNthNode(self, index):
        current = self.head
        print("incoming node ", current.data)
        count = 0
        
        while current: #last is not reached
            if count == index:
                return current.data
            count += 1
            current = current.next
            print("get_nth_index ", current.data, current.next.data, count)
        return None

# Driver Code 
if __name__ == '__main__': 
  
    llist = LinkedList() 
  
    # Use push() to construct below list 
    # 1->12->1->4->1 
    llist.push(1) 
    llist.push(4) 
    llist.push(2) 
    llist.push(12) 
    llist.push(3) 
  
    n = 3
    print("Element at index 3 is :", llist.getNthNode(n))