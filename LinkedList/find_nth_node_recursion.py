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

    # option 1
    # def getNthNode(self, current_node, index):
    #     if not current_node: #  If the current node is None, return None. This handles the case where the index is out of bounds.
    #         return None
    #     if index == 0:
    #         return current_node.data
    #     return self.getNthNode(current_node.next, index-1)

    # option 2
    def _getNthNodeHelper(self, current_node, index):
        if not current_node: #  If the current node is None, return None. This handles the case where the index is out of bounds.
            return None
        if index == 0:
            return current_node.data
        return self._getNthNodeHelper(current_node.next, index-1)
    
    def getNthNode(self, index):
        self._getNthNodeHelper(self.head, index)

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
    # option 1
    # print("Element at index 3 is :", llist.getNthNode(llist.head,n))

    #option 2
    print("Element at index 3 is :", llist.getNthNode(n))