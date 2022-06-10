# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        lllen = 0
        while curr:
            curr = curr.next
            lllen += 1
        print(lllen)

        mid = lllen//2
        if lllen == 1:
            return head
        i = 0
        curr = head
        while i != mid:
            curr = curr.next
            i += 1
            if i == mid:
                return curr
