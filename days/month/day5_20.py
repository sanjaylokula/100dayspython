# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        def t(d):
            if d.next:
                if d.next.val == val:
                    d.next = d.next.next
                    t(d)
                else:
                    t(d.next)

        t(dummy)
        return dummy.next


if __name__=="__main__":
    output=Solution().removeElements([1,2,6,3,4,5,6],6)
    print(output)