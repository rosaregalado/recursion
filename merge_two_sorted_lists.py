# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


class Solution(object):
  def mergeTwoLists(self, list1, list2):
    # base case
    if not list1:
      return list2
    elif not list2:
      return list1

    # compare the heads of both lists
    # whichever head is smaller becomes the new head of the merged list
    
    #  if list2 is larger, list 1 becomes new head
    if list1.val < list2.val:
      list1.next = self.mergeTwoLists(list1.next, list2)
      return list1
    else:
      list2.next = self.mergeTwoLists(list1, list2.next)
      return list2


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# merge the linked lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# print the merged list
while merged_list:
  print(merged_list.val)
  merged_list = merged_list.next