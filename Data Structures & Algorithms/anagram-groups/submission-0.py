class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana = {}

        for s in strs:
            sortedS = ''.join(sorted(s))

            if sortedS not in ana:
                ana[sortedS] = []
            
            ana[sortedS].append(s)

        return list(ana.values())