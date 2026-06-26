class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            else:
                count2 += 1
        j = 0
        for k in range(count0):
            nums[j] = 0
            j += 1
        for k in range(count1):
            nums[j] = 1
            j += 1
        for k in range(count2):
            nums[j] = 2
            j += 1