class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = nums.count(0)
        res = 1
        final = []
        for i in nums:
            if i != 0:
                res *= i

        for x in nums:
            if zero > 1:
                final.append(0)
            elif zero ==1:
                final.append(res if x == 0 else 0)
            else:
                final.append(res//x)

        return final