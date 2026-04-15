class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, right = 0, 0
        len_substring = 0
        lastIndex = {}

        while right < len(s):

            if s[right] in lastIndex:
                left = max(left, lastIndex[s[right]] + 1)

            lastIndex[s[right]] = right
            len_substring = max(len_substring, right - left + 1)
            right += 1
            

        return len_substring




        