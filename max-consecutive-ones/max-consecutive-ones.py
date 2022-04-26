class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        windows = []
        start = False
        count = 0
        for num in nums:
            if num==1:
                start = True
                count +=1
            else:
                start = False
                windows.append(count)
                count = 0
        
        if nums[-1]==1:
            windows.append(count)
        print(windows)
        return max(windows)