class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_s = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            dict_s[sorted_s].append(s)
        
        return list(dict_s.values())

