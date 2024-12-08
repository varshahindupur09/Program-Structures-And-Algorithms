# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n), as we traverse the list once.
# Space Complexity: O(1), as no additional space is used except for pointers.

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftprev, curr = dummy, head
        # just before left
        # itr1: leftprev = 1, curr = 2
        for _ in range(left - 1):
            leftprev, curr = curr, curr.next #1,2

        prev = None
        for _ in range(right - left + 1): #3 #2
            # 1 -> 2 (reversed to None)   3 -> 4 -> 5
            # 1 -> 3 -> 2 (reversed)   4 -> 5
            tmpNext = curr.next #tempNex = 3 #tempN=4
            curr.next = prev # 3=>null #4=>2
            prev, curr = curr, tmpNext #prev=>2,curr=>3 #prev=3,curr=5

        leftprev.next.next = curr
        leftprev.next = prev
        return dummy.next
            

        


