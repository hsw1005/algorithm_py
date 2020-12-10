# re

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, data, next=None):
        self.datat = data
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    def add(self, data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = None(data)

def mergeTwoLists(list1, list2):

mergeTwoLists(list1, list2)