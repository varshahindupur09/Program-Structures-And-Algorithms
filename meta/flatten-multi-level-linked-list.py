import heapq

class ListNode:
    def __init__(self, data=0, next=None, down=None):
        self.data = data
        self.next = next
        self.down = down

    # Optional: For easier debug printing
    def __lt__(self, other):
        return self.data < other.data
#################################
1 → 5 → 8
↓   ↓   ↓
3   8   14
↓       ↓
8       26
#################################

class Solution:
    def flattenTheLinkedList(self, root: ListNode) -> ListNode:
        if not root:
            return None

        min_heap = []
        counter = 0  # To avoid comparison issues if values are equal

        # Push all top-level nodes into the heap
        curr = root
        while curr:
            heapq.heappush(min_heap, (curr.data, counter, curr))
            counter += 1
            curr = curr.next

        dummy = ListNode(-1)
        tail = dummy

        while min_heap:
            _, _, node = heapq.heappop(min_heap)

            tail.down = ListNode(node.data)
            tail = tail.down

            if node.down:
                heapq.heappush(min_heap, (node.down.data, counter, node.down))
                counter += 1

        return dummy.down

#################################
430: Flatten a Multilevel Doubly Linked List
#################################

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head

        while node:
            if node.child:
                old_next = node.next
                node.next = self.flatten(node.child)
                node.next.prev = node
                node.child = None

                while node.next: # child node has more children
                    node = node.next 
                node.next = old_next
                if old_next:
                    old_next.prev = node

            node = node.next

        return head

            

