"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

* Example 1:
	- Input: nums = [5,7,7,8,8,10], target = 8
	- Output: [3,4]

* Example 2:
	- Input: nums = [5,7,7,8,8,10], target = 6
	- Output: [-1,-1]

* Example 3:
	- Input: nums = [], target = 0
	- Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 找出target在list裡最小的ndex位置
        left = self.lower_bound(nums, target)   
        # 找出target在list裡最大的index再往右一個的位置
        right = self.upper_bound(nums, target)  
        if left == right:
            return [-1, -1]
        return [left, right - 1]
        
        
    # 當mid < target時，才移動left指標
    def lower_bound(self, nums: list, target: int):
        left, right = 0, len(nums)
        while left < right:
            mid = (right - left)//2 + left
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


    # 當mid <= target時，就移動left指標
    def upper_bound(self, nums: list, target: int):
        left, right = 0, len(nums)
        while left < right:
            mid = (right - left)//2 + left
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left    