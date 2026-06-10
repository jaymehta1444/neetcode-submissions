class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        get = []

        for key, value in count.items():
            get.append([value, key])

        get.sort()

        result = []

        while len(result) < k:
            result.append(get.pop()[1])

        return result