class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        values.sort()
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next
