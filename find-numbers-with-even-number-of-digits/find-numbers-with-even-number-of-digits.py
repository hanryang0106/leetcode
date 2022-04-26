class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digits = [len(str(num)) for num in nums]
        ans = sum(i % 2 == 0 for i in digits)
        return ans
            