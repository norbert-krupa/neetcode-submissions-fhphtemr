class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs == []:
            return ""

        longestPrefix = ""
        checkChar = 0
        shortestStr = len(min(strs))

        for i in range(shortestStr):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j+1][i]:
                    return longestPrefix
            longestPrefix += strs[0][i]


        return longestPrefix

        