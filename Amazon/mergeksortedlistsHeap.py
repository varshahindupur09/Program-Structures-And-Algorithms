# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # k * Log K
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        # n * log K
        while heap:
            value, i, node = heapq.heappop(heap)
            # print(value, i, node)
            # 1 0 ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
            # 1 1 ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
            # 2 2 ListNode{val: 2, next: ListNode{val: 6, next: None}}
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return dummy.next


# TC: O(nlogK)
# SC: O(k)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
TC, SC = n log k
Brute Force = O(n * k)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
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

