"""
* [367. Valid Perfect Square] (完全平方數)
* 題目：
    - 判斷一個正整數是否為完全平方數
    - 限制：不可使用sqrt()
* ex1:
    - Input: num = 16
    - Output: true
* ex2:
    - Input: num = 14
    - Output: false
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid*mid > num:
                right = mid - 1
            elif mid*mid < num:
                left = mid + 1
            else:
                return True
        return False