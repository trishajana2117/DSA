class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_right = 0
        for i , x in enumerate(nums):
            if i > furthest_right:
                return False
            furthest_right = max(furthest_right, i+x)
        return True