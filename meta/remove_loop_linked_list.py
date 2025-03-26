# detect loop with floyd's algorithm
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def detectCycle(head):
    slow = fast = head

    # Step 1: Detect if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            break
    else:
        return None  # No cycle

    # find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Start of the cycle

# remove loop
def detectCycle(head):
    slow = fast = head
    loop_exists = False

    # Step 1: Detect Loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_exists = True
            break

    if not loop_exists:
        return  # No loop

    # Step 2: Find start of loop
    slow = head
    if slow == fast:
        # Special case: loop starts at head
        while fast.next != slow:
            fast = fast.next
    else:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

    # Step 3: Break the loop
    fast.next = None
    

