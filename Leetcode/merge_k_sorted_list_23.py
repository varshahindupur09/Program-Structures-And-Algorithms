import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:    
    def mergeLists(self, lists: List[Optional[ListNode]]):
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode()
        curr = dummy
        print(heap)

        while heap:
            value, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        return dummy.next

    def build_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def print_linked_list(self, node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        print(values)

s = Solution()
lists = [s.build_linked_list([1,4,5]),s.build_linked_list([1,3,4]),s.build_linked_list([2,6])]
merged = s.mergeLists(lists)
s.print_linked_list(merged)


#######################################################################################################
solution 2
#######################################################################################################

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(l1, l2))
            lists = temp
        
        return lists[0]
    
    def merge_lists(self, l1, l2):
        node = ListNode()
        ans = node
        
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        
        if l1:
            node.next = l1
        else:
            node.next = l2
        
        return ans.next

