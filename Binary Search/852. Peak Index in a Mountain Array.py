"""
- [852. Peak Index in a Mountain Array] (尋找山頂)
- 題目：
    - 給一個array，其中會有一個數為山頂，在山頂之前的數字會漸漸增加，在山頂之後的數字會漸漸減少。請找出山頂的index值。
    - 請勿使用max()或index()，嘗試用二元搜尋法來作。
- ex1:
    - Input: arr = [0,1,0]
    - Output: 1
- ex2:
    - Input: arr = [0,2,1,0]
    - Output: 1
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid] < arr[mid - 1]:
                right = mid - 1
            else:
                return mid