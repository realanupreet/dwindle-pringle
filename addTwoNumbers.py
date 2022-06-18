# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ourl1 = l1
        nl1 = []
        while ourl1:
            nl1.append(ourl1.val)
            ourl1 = ourl1.next
        nl1 = int("".join(str(i) for i in reversed(nl1)))
        # print(nl1)

        ourl2 = l2
        nl2 = []
        while ourl2:
            nl2.append(ourl2.val)
            ourl2 = ourl2.next
        nl2 = int("".join(str(i) for i in reversed(nl2)))
        # print(nl2)
        nl3 = nl1+nl2
        res = [int(x) for x in str(nl3)]
        res = reversed(res)
        l3 = head = ListNode()
        # l3 = l1
        for i in res:
            l3.next = ListNode(i)
            l3 = l3.next
        return head.next
