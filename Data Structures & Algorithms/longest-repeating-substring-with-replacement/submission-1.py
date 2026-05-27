class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, right = 0, 0
        len_substring = 0
        charFreq = {}

        while right < len(s):
            charFreq[s[right]] = charFreq.get(s[right], 0) + 1

            if not (right - left + 1) - (max(charFreq.values())) <= k:
                charFreq[s[left]] -= 1
                left += 1

            len_substring = max(len_substring, (right - left) + 1)
            right += 1

        return len_substring