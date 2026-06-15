class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        nums_set = set(nums)
        consider = []
        final = []

        for n in nums_set:
            if n - 1 in nums_set:
                continue
            consider.append(n)

        for i in consider:
            count = 1
            current = i

            while current + 1 in nums_set:
                current += 1
                count += 1

            final.append(count)

        return max(final)