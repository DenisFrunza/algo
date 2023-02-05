#https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = current = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2
        return merged.next

#https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1

# https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: 
            return False
        
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next: return False
            slow, fast = slow.next, fast.next.next
        return True

#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left != right:
            if sum((numbers[left], numbers[right])) == target:
                return [left+1, right+1]
            if sum((numbers[left], numbers[right])) > target:
                right -= 1
            else:
                left += 1

        return -1
#https://leetcode.com/problems/palindrome-linked-list/
class Node:

	def __init__(self, data):

		self.value = data
		self.next = None


class LinkedList:


	def __init__(self):

		self.head = None

	def push(self, new_data):

		new_node = Node(new_data)

		new_node.next = self.head

		self.head = new_node


def reverse(second_half):
    prev = None
    current = second_half
    next = None

    while current != None:
        next = current.next
        current.next = prev
        prev = current 
        current = next
        
    return prev

def compare_list(l1, l2):
    tmp1 = l1
    tmp2 = l2

    while tmp1 and tmp2:
        if tmp1.value == tmp2.value:
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        else:
            return False
    return True

def is_palindrome(head):
    list_size = 0
    copy_head = head
    while head:
        head = head.next
        list_size += 1
    
    counter = 0
    first_part = copy_head
    second_half = None
    while first_part:
        counter += 1
        if counter > list_size // 2:
          second_half = first_part
          break
        else:
            first_part = first_part.next

    reversed_second_half = reverse(second_half=second_half)

    res = compare_list(l1=copy_head, l2=reversed_second_half)
    return res


def solution(l):
    return is_palindrome(head=l)

#https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len( nums) <= 1:
            return nums
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums

# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point_1 = head
        point_2 = head
        while point_2 and point_2.next:
            point_1 = point_1.next
            point_2 = point_2.next.next

        return point_1

# https://leetcode.com/problems/delete-node-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        if key > root.val:
           root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key == root.val:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            root.right = self.lift(root.right, root)
        return root

    def lift(self, node, node_to_delete):
        if node.left:
            node.left = self.lift(node.left, node_to_delete)
            return node
        else:
            node_to_delete.val = node.val
            return node.right
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current_node = root
        while current_node:
            if current_node.val == val:
                return current_node
            if val > current_node.val:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return None
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right =  self.insertIntoBST(root.right, val)
        
        return root
# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q

        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right

# https://leetcode.com/problems/symmetric-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_the_tree_symmetric(root.left, root.right)
    
    def is_the_tree_symmetric(self, left, right):
        if left is None and right is None:
            return True

        if left and right and left.val == right.val:
            return self.is_the_tree_symmetric(left.left, right.right) and self.is_the_tree_symmetric(right.left, left.right)

        return False