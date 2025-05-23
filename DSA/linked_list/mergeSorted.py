class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val 
        self.next = next

class Merge:
    def merge(self , list1:ListNode , list2:ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2 :
            if list1.val < list2.val:
                tail.next = list1.val
                list1 = list1.next

            else:
                tail.next = list2.val
                list2 = list2.next

            tail = tail.next 

        if list1 :
            tail.next = list1.val

        if list2:
            tail.next = list2.val

        return dummy.next
    


