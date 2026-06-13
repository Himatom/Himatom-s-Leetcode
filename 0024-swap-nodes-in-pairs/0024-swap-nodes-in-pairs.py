class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr and curr.next:
            nxt_pair = curr.next.next
            second = curr.next
            
            second.next = curr
            curr.next = nxt_pair
            prev.next = second
            
            prev = curr
            curr = nxt_pair
            
        return dummy.next