# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        print("arr is", arr)

        for i in range(0, len(arr)):
            if arr[i] != arr[-(i+1)]:
                # print(f"{arr[i]} {i} != {arr[-(i+1)]} {-(i+1)}")
                return False
        return True
