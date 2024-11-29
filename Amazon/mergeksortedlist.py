###########################################################################
21 https://leetcode.com/problems/merge-two-sorted-lists/
###########################################################################

# TC: O(n+m)
# SC: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


###########################################################################
23 https://leetcode.com/problems/merge-k-sorted-lists/
###########################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # k Log K
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        # n log K
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
