#########################################################################################################
# detect cycle in singly-linked list
#########################################################################################################

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        curr = head
        while curr:
            if curr in node_set:
                return True
            node_set.add(curr)
            curr = curr.next


########################################################################################################
# detect cycle in singly-linked list using fast and slow pointers (Floyd's Cycle Detection Algorithm)
########################################################################################################

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
# Space Complexity: O(1)
# Time Complexity: O(n)

########################################################################################################
#  Reason why this happens: at first it moves normally and then it cycles through
########################################################################################################
Cycle Mechanics:
To illustrate the cycle specifically:

markdown
Copy code
3 -> 4 -> 2 -> 1
|______________|
Normal Moves: 3 → 4 → 2 → 1.

After the Cycle: 1 → 3 → 4 → 2 → 1 → 3 → ... (repeats infinitely).

The fast pointer’s two-step logic causes it to loop back through the cycle until it catches up with the slow pointer.
