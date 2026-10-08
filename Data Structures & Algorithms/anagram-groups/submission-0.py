from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
         
        for s in strs:
            x = "".join(sorted(s))
            anagrams[x].append(s)

        return list(anagrams.values())
