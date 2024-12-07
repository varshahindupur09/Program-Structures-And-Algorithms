####################################################################################
SOLUTION
####################################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# reverse the linked list to get palindrome
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # traverse to the second last or middle position of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the linked list into prev
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # now check for palidrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
