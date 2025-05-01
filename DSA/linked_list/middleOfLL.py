# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        slow , fast = head , head
        prev = None

        if head is None or head.next is None:
            return None 

        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast = fast.next.next

        return slow 
    

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()

result = solution.deleteMiddle(head)

print(result.val)
while head:
    print(head.val)
    head = head.next