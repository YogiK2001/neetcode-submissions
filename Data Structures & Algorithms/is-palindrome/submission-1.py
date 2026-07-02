class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_chars = [char.lower() for char in s if char.isalnum()]
        clean_s = "".join(new_chars)

        if clean_s ==  clean_s[::-1]:
            return True
        return False
