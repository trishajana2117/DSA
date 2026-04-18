class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        no = 0
        for i in digits:
            no = no * 10 + i
        no += 1
        return [int(x) for x in str(no)]