class ListNode:
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next

class Slist:
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0

    # append: add a node at the end of the slist # Time: THETA(1) and  Space: THETA(1)
    def append(self, value: int):
        self._len = self._len + 1
        self._build_a_node(value, True)
        
    # prepend: add a node at the beginning of the slist # Time: THETA(1) and  Space: THETA(1)
    def prepend(self, value: int):
        self._len = self._len + 1
        self._build_a_node(value, False)

    def _unhook(self, nodes: list) -> bool:
        if nodes[0]:
            currentnode = nodes[0]
            previousnode = nodes[1]
            if (currentnode == self._first) and (currentnode == self._last) and (previousnode is None):
                # list has only 1 element
                assert self._first == self._last
                self._first = None
                self._last = None
            elif currentnode == self._first:
                # first element being removed and list has more than 1 element
                assert self._first.next is not None
                self._first = currentnode.next  # Corrected: update _first correctly
            elif currentnode == self._last:
                # last element being removed and list has more than 1 element
                assert self._first
                previousnode.next = None
                self._last = previousnode
            else:
                # you're removing middle element
                assert self._first
                assert self._last
                previousnode.next = currentnode.next
            self._len = self._len - 1
            return True
        else:
            return False
        
    def delete(self, value: int) -> bool:
        nodes = self._find(value)
        a = self._unhook(nodes)
        return a

    # first element in slist # Time: THETA(1) and  Space: THETA(1)
    def delete_front(self) -> bool:
        if self._first:
            nodes = [self._first, None]
            a = self._unhook(nodes)
            return a
        else:
            return False
        
    # get first element in slist # Time: THETA(1) and  Space: THETA(1)
    def get_front(self):
        if self._first:
            return self._first.data
        else:
            return -1  # Corrected: return -1 instead of False
    
    # get last element in slist # Time: THETA(1) and  Space: THETA(1)
    def get_last(self):
        if self._first:
            assert self._last
            return self._last.data
        else:
            return -1  # Corrected: return -1 instead of False
        
    # delete element in slist # Time: THETA(n) and  Space: THETA(1)
    def delete_last(self) -> bool:
        if self._first:
            nodes = [self._first, None]
            # list of [currentnode, prevnode]
            while nodes[0].next:
                nodes[1] = nodes[0]
                nodes[0] = nodes[0].next
            
            assert nodes[0]
            assert nodes[0].next is None
            # if nodes[1]:
            #     assert nodes[0].next == nodes[0]
            a = self._unhook(nodes)
            return a
        else:
            return False

    # is slist empty # Time: THETA(1) and Space: THETA(1)
    def is_empty(self) -> bool:
        return self._len == 0

    # number of elements in a list # Time: THETA(1) and Space: THETA(1)
    def __len__(self) -> int:
        return self._len

    # build a node and add to end/beginning #Time; THETA(1) and Space: THETA(1)
    def _build_a_node(self, i: int, append: bool = True):
        n = ListNode(i)
        if self._first is None and self._last is None:  # handle empty case
            self._first = n
            self._last = n
        else:
            if append:
                self._last.next = n
                self._last = n
            else:
                n.next = self._first
                self._first = n

    # find an element in slist # Time: O(n) and Space: THETA(1)
    def _find(self, val: int) -> list:
        nodes = [self._first, None]
        while nodes[0] is not None:
            if nodes[0].data == val:
                return nodes
            nodes[1] = nodes[0]
            nodes[0] = nodes[0].next
        return nodes

print("---------- solution 1: Answer Leetcode 225 -------------")
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyStack:
    def __init__(self):
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s.prepend(x)
    
    def pop(self):
        val = self._s.get_front()
        self._s.delete_front()
        return val

    def top(self) -> int:
        return self._s.get_front()
    
    def empty(self) -> bool:
        l = len(self._s)
        if l==0:
            return True
        return False

print("---------- solution 2: Answer Leetcode 235 -------------")   
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class MyQueue:
    def __init__(self):
        self._s = Slist()

    def push(self, x: int) -> None:
        self._s.append(x)

    def pop(self) -> int:
        xvalue = self._s.get_front()
        self._s.delete_front()
        return xvalue
    
    def peek(self) -> bool:
        return self._s.get_front()

    def empty(self) -> bool:
        l = len(self._s)
        if l==0:
            return True
        return False

print("---------- solution 3: Answer Leetcode 622 -------------")   
# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
    def __init__(self, k: int):
        self._s = Slist()
        self._K = k
    
    def isEmpty(self) -> bool:
        l = len(self._s)
        if l==0:
           return True
        return False

    def isFull(self) -> bool:
        l = len(self._s)
        if self._K == l:
           return True
        return False

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.append(value)
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._s.delete_front()
        return True

    def Front(self) -> int:
        return self._s.get_front()
    
    def Rear(self) -> int:
        return self._s.get_last()
    

print("---------- solution 4: Answer Leetcode 641 -------------")   
# https://leetcode.com/problems/design-circular-deque

class MyCircularDeque:
    def __init__(self, k: int):
        self._s = Slist()
        self._K = k

    def isEmpty(self) -> bool:
        return self._s.is_empty()
    
    def isFull(self) -> bool:
        return self._K == len(self._s)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.prepend(value)
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self._s.append(value)
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self._s.delete_front()
        return True
    
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        return self._s.delete_last()

    def getFront(self) -> int:
        return self._s.get_front()
    
    def getRear(self) -> int:
        return self._s.get_last()