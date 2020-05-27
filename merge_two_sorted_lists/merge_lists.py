# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nex=None):
        self.val = val
        self.next = nex


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr_l1 = l1
        curr_l2 = l2

        while curr_l1 != None and curr_l2 != None:
            if curr_l1.val <= curr_l2.val:
                old_next = curr_l1.next
                curr_l1.next = curr_l2
                curr_l1 = old_next
            else:
                old_next = curr_l2.next
                curr_l2.next = curr_l1
                curr_l2 = old_next
        return l1


# tests
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node4.next = node5
node5.next = node6

test = Solution()
test_list = test.mergeTwoLists(node1, node4)
while test_list != None:
    print(test_list.val)
    test_list = test_list.next
