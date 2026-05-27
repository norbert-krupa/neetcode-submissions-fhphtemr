class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left, right = 0, 0
        len_substring = 0
        charFreq = {
            "A" : 0,
            "B" : 0,
            "C" : 0,
            "D" : 0,
            "E" : 0,
            "F" : 0,
            "G" : 0,
            "H" : 0,
            "I" : 0,
            "J" : 0,
            "K" : 0,
            "L" : 0,
            "M" : 0,
            "N" : 0,
            "O" : 0,
            "P" : 0,
            "Q" : 0,
            "R" : 0,
            "S" : 0,
            "T" : 0,
            "U" : 0,
            "V" : 0,
            "W" : 0,
            "X" : 0,
            "Y" : 0,
            "Z" : 0
        }

        while right < len(s):
            charFreq[s[right]] += 1
            
            if not (right - left + 1) - (max(charFreq.values())) <= k:
                charFreq[s[left]] -= 1
                left += 1

            len_substring = max(len_substring, (right - left) + 1)
            right += 1

        return len_substring