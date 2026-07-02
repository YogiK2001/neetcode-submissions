class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_chars = [char.lower() for char in s if char.isalnum()]
        clean_s = "".join(new_chars)

        left, right = 0, len(clean_s)-1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        return True