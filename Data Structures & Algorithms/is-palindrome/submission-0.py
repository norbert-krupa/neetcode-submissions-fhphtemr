class Solution:
    def isPalindrome(self, s: str) -> bool:

        valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        s_clean = "".join([c.lower() for c in s if c in valid_chars and c != " "])
        left, right = 0, len(s_clean) - 1

        while left < right:
            if s_clean[left] != s_clean[right]:
                return False

            left += 1
            right -= 1

        return True
