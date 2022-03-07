"""
- [744. Find Smallest Letter Greater Than Target] (尋找字元)
- 題目：
    - 給定一個target字元與一個字元序列，該序列按非遞減的順序，在序列中找出一個字元，而該字元是比target字元大的最小字元。字元大小順序是由a,b,c…z，z之後再連回a,b,c…。
    - 舉例：
        - 字元序列為[‘a’, ‘b’]，而target字元為z，要在字元序列中找比z大的最小字元，答案是a。
    - ex1:
        - Input: letters = [“c”,“f”,“j”], target = “a”
        - Output: “c”
    - ex2:
        - Input: letters = [“c”,“f”,“j”], target = “c”
        - Output: “f”
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[len(letters) - 1]:
            return letters[0]
        
        left, right = 0, len(letters) - 1
        while left < right:
            mid = (left + right) // 2
            if letters[mid] == target:
                if letters[mid+1] != target:
                    return letters[mid + 1]
                else:
                    left = mid + 2
            elif letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        return letters[left]